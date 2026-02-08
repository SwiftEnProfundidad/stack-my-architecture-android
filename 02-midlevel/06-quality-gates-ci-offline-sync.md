# Nivel Midlevel · 06 · Quality Gates en CI para proteger offline-sync en cada PR

A esta altura del roadmap ya no estás construyendo “pantallas sueltas”. Ya tienes decisiones de arquitectura, sincronización, observabilidad y pruebas de integración que representan dinero y confianza del producto. El problema real que aparece ahora no es técnico de implementación, es de gobernanza: cómo evitar que una mejora aparentemente inocente rompa `offline-first` el viernes por la noche y llegue a producción el lunes.

La respuesta madura a ese problema es dejar de confiar en la memoria humana y mover las reglas críticas a automatización de CI. Cuando hablamos de quality gates no hablamos de burocracia, hablamos de convertir aquello que no quieres romper en un contrato verificable antes de mergear.

Este módulo existe para eso. Vas a salir con un pipeline que valida formato, compilación y pruebas clave de sincronización, y que falla de forma explícita cuando algo importante se degrada.

---

## El principio que manda aquí

Si tu flujo offline-sync es importante para negocio, no puede depender de “yo lo probé en mi máquina”. Necesita una puerta automática que diga sí o no con reglas transparentes. Esa puerta es el quality gate.

La consecuencia práctica es simple: cada pull request debe demostrar dos cosas antes de entrar en `main`. Debe ser técnicamente sano, y debe conservar el comportamiento que prometimos al usuario cuando no hay red.

Con esa intención clara, vamos a implementarlo sin adornos.

---

## Qué vamos a automatizar en este primer gate

En este punto del curso todavía no necesitamos un pipeline enorme. Lo que sí necesitamos es un pipeline que ya tenga dientes y bloquee regresiones reales. Por eso vamos a exigir que el código formatee y compile bien, y que pase la suite que acabas de crear para offline-sync.

Eso significa que una PR que rompa la transición `PENDING -> SYNCED` no podrá entrar, aunque localmente alguien no se haya dado cuenta.

---

## Crear workflow de GitHub Actions

Dentro del repo Android crea el archivo `.github/workflows/android-quality-gates.yml`.

```yaml
name: Android Quality Gates

on:
  pull_request:
    branches: [ "main" ]
  push:
    branches: [ "main" ]

jobs:
  quality-gates:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup JDK 17
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 17
          cache: gradle

      - name: Setup Gradle
        uses: gradle/actions/setup-gradle@v4

      - name: Validate Gradle Wrapper
        uses: gradle/wrapper-validation-action@v3

      - name: Kotlin lint check
        run: ./gradlew ktlintCheck

      - name: Compile debug
        run: ./gradlew assembleDebug

      - name: Run offline-sync integration tests
        run: ./gradlew :features:tasks:test --tests "*TasksOfflineSyncIntegrationTest"
```

Este YAML es corto, pero está pensado para un problema concreto. Primero asegura un entorno limpio y repetible. Luego valida que el wrapper no fue manipulado, porque el wrapper es parte de la superficie de seguridad del build. Después ejecuta `ktlintCheck`, que evita deuda de estilo creciendo silenciosamente. A continuación compila `assembleDebug`, que detecta incompatibilidades estructurales entre módulos. Y por último ejecuta exactamente la suite de integración que protege el corazón offline-sync.

La decisión de no correr “todo” en este primer gate está hecha a propósito. Un gate útil tiene que ser rápido y confiable. Si lo vuelves lento e inestable desde el primer día, la gente aprende a odiarlo y a buscar bypass. Aquí queremos lo contrario: señal temprana, estable y con impacto real.

---

## Alinear Gradle para que el gate sea reproducible

Ahora asegúrate de que el proyecto tiene tasks de calidad consistentes, especialmente `ktlintCheck`. Si ya lo tienes con tu plugin de lint actual, perfecto. Si no lo tienes todavía, añade una configuración mínima en `build.gradle.kts` del root.

```kotlin
plugins {
    id("org.jlleitschuh.gradle.ktlint") version "12.1.1"
}

subprojects {
    apply(plugin = "org.jlleitschuh.gradle.ktlint")
}
```

La razón de esta decisión no es estética. Es reducir ruido cognitivo en PRs. Cuando el formato queda automatizado, las revisiones dejan de discutir espacios y pasan a discutir decisiones técnicas. Además, CI y local se comportan igual porque ambos ejecutan la misma tarea.

Si en tu repo ya existe Spotless u otra herramienta equivalente, no dupliques herramientas. Mantén una sola fuente de verdad para estilo. Lo importante del gate no es el nombre de la task, sino la consistencia.

---

## Endurecer la ejecución de pruebas para evitar falsos verdes

Ahora vamos a endurecer ligeramente la ejecución de test JVM para que CI falle con más honestidad cuando hay problemas de concurrencia o tests frágiles.

En el módulo donde vive `TasksOfflineSyncIntegrationTest`, revisa `build.gradle.kts` y añade:

```kotlin
tasks.withType<Test>().configureEach {
    useJUnit()
    testLogging {
        events("passed", "failed", "skipped")
        showExceptions = true
        showCauses = true
        showStackTraces = true
    }
    failFast = true
}
```

Aquí `failFast = true` tiene una intención muy práctica: cuando algo crítico cae, no desperdicias minutos ejecutando más casos que no cambian la decisión final de merge. En PRs con mucho movimiento eso ahorra tiempo y feedback loop.

`testLogging` con stacktraces completas te evita ese clásico momento donde CI marca rojo y nadie entiende por qué. En calidad, la claridad del fallo vale casi tanto como el fallo en sí.

---

## Convertir este gate en contrato de equipo

Automatizar sin acordar reglas deja huecos de proceso. Necesitas una regla explícita: “si el gate falla, no se mergea”.

Esa regla no va en una reunión, va en el repositorio. Crea `docs/quality-gates.md` con el acuerdo operativo.

```md
# Quality Gates Android

Este repositorio no permite merge a main si falla el workflow `Android Quality Gates`.

El gate valida:
- lint Kotlin
- compilación debug
- pruebas de integración offline-sync (`TasksOfflineSyncIntegrationTest`)

Si falla cualquiera de estos puntos, la PR debe corregirse antes de merge.
```

Observa lo importante: el documento no es largo, pero elimina ambigüedad. Lo que antes era una expectativa informal ahora es una política auditable.

---

## Ejecutarlo en local antes de abrir PR

Para que la experiencia del equipo sea buena, nadie debería enterarse en CI de un fallo fácil de detectar en su máquina. Por eso conviene correr el mismo gate localmente.

```bash
./gradlew ktlintCheck assembleDebug :features:tasks:test --tests "*TasksOfflineSyncIntegrationTest"
```

Ese comando replica el corazón del workflow. Si pasa local, normalmente pasará en CI salvo diferencias de entorno o dependencias externas.

Este hábito reduce ciclos de “push, falla, arregla, push” y mejora mucho el ritmo de entrega cuando hay varios desarrolladores tocando la misma base.

---

## Qué comportamiento ya estás protegiendo de verdad

Con este módulo no solo agregaste un YAML. Lo que hiciste fue blindar un riesgo de negocio. Si alguien toca mapping de sync, o cambia estado de entidad, o mueve lógica del orquestador de forma incorrecta, el pipeline lo detecta antes de que llegue a producción.

Eso cambia la dinámica del proyecto. Tu arquitectura deja de ser “una buena intención en documentos” y pasa a ser “un sistema con frenos automáticos”. Y en equipos reales, esa diferencia es enorme.

---

## Cómo saber que quedó bien implementado

Cuando abras una PR de prueba, deberías ver el workflow `Android Quality Gates` ejecutándose automáticamente. Si haces una ruptura intencional en la suite de integración, la ejecución debe quedar en rojo. Si corriges y subes de nuevo, debe volver a verde.

Esa prueba de fuego es clave. Un gate que nunca falla suele ser un gate decorativo.

---

## Cierre del módulo

Has llegado a un punto donde el roadmap da un salto de madurez: ya no solo construyes funcionalidades, también construyes mecanismos para que la calidad se sostenga mientras el proyecto crece. Ese cambio de mentalidad es una marca clara de perfil midlevel sólido.

En el siguiente tramo del roadmap vamos a conectar este gate con medición de rendimiento real en CI usando Macrobenchmark y Baseline Profiles, para que no solo protejas corrección funcional, sino también experiencia de usuario bajo carga y tiempos de arranque.
