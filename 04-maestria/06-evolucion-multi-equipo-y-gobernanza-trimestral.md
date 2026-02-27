# Nivel Maestría · 06 · Evolución multi‑equipo y gobernanza trimestral en Android

Cuando un producto Android entra en una etapa donde varios equipos empujan cambios al mismo tiempo, la arquitectura deja de ser solo una cuestión de diseño técnico y pasa a ser una cuestión de coordinación. La sensación típica en ese momento es conocida: cada equipo “va bien” dentro de su propio backlog, pero el sistema completo empieza a perder coherencia. No porque la gente trabaje mal, sino porque falta un marco común para decidir qué se puede mover en paralelo y qué necesita sincronización explícita.

Esta lección aterriza ese punto. No vamos a hablar de gobernanza como burocracia, sino como mecanismo para sostener velocidad sin sacrificar estabilidad. La idea central es simple: si la arquitectura define límites, la gobernanza define cómo evolucionan esos límites con el tiempo.

Piensa en tres equipos trabajando durante el mismo trimestre. Uno está migrando contratos de perfil, otro evoluciona checkout y el tercero cambia rutas de navegación para soporte de deep links nuevos. Si cada uno optimiza su tramo sin mirar dependencias activas, lo que aparece en producción es una mezcla difícil de depurar: incompatibilidades suaves, fallos intermitentes y rollback parciales que no terminan de limpiar el estado.

El antídoto real no es parar todo y coordinar cada mínimo cambio. El antídoto es acordar un ritmo de integración con reglas claras de compatibilidad temporal. Eso permite que cada equipo mantenga autonomía diaria, pero dentro de un carril compartido que evita sorpresas sistémicas.

Una forma práctica de materializar ese carril es definir un calendario de ventanas técnicas por trimestre. No es un calendario para “reuniones infinitas”, sino para decisiones críticas que sí necesitan convergencia. En esas ventanas se acuerda qué contratos entran en convivencia dual, qué features quedan protegidas por freeze parcial y qué métricas habilitan la siguiente fase.

```kotlin
package com.stackmyarchitecture.governance

data class QuarterlyArchitectureWindow(
    val quarter: String,
    val migrationName: String,
    val compatibilityStart: String,
    val compatibilityEnd: String,
    val owningTeam: String
)

data class MigrationDecision(
    val migrationName: String,
    val proceedToNextPhase: Boolean,
    val rationale: String,
    val approvedBy: String
)
```

Este modelo no intenta reemplazar herramientas de gestión. Lo que hace es capturar decisiones de arquitectura con un lenguaje consistente. Eso resuelve un problema de fondo: cuando semanas después alguien pregunta por qué se mantuvo compatibilidad de una versión antigua, no depende de memoria oral. Hay trazabilidad explícita.

Otro problema habitual en escalado multi‑equipo es que cada squad usa métricas distintas para declarar “éxito”. Un equipo mira crash rate, otro mira latencia y otro solo mira si pasó CI. El resultado es que no existe una definición compartida de “listo para avanzar”. Por eso conviene acordar un contrato de salud técnica transversal.

```kotlin
package com.stackmyarchitecture.governance

data class MigrationHealthSnapshot(
    val migrationName: String,
    val adoptionPercent: Double,
    val errorRateP95: Double,
    val latencyP95Ms: Long,
    val rollbackCount: Int
)

interface MigrationGate {
    fun canAdvance(snapshot: MigrationHealthSnapshot): Boolean
}

class ConservativeMigrationGate : MigrationGate {
    override fun canAdvance(snapshot: MigrationHealthSnapshot): Boolean {
        return snapshot.adoptionPercent >= 0.95 &&
            snapshot.errorRateP95 <= 0.01 &&
            snapshot.latencyP95Ms <= 350 &&
            snapshot.rollbackCount == 0
    }
}
```

Aquí la decisión importante no es el número exacto de cada umbral. Lo importante es que todos los equipos juegan con la misma regla para pasar de fase. Eso evita discusiones estériles en momentos de presión y convierte la evolución en un proceso verificable.

Cuando este marco no existe, la deuda aparece en un lugar muy concreto: excepciones eternas. Un equipo pide mantener una compatibilidad “solo una semana más”, otro también, y sin darte cuenta acabas con una arquitectura que arrastra decisiones temporales durante meses. Por eso una gobernanza sana no solo aprueba excepciones; también fija fecha de retiro y owner de salida.

En Android esto importa especialmente porque el ecosistema de dispositivos y versiones añade variabilidad real. Si no pones límites temporales a las excepciones, cada release hereda complejidad acumulada y el coste de pruebas se dispara. El equipo siente que cada entrega pesa más que la anterior, aunque el alcance funcional sea parecido.

La comunicación entre equipos también cambia cuando la gobernanza está madura. Deja de ser “aviso informal por chat” y pasa a ser una narrativa técnica breve y repetible: estado actual, riesgo principal, decisión tomada y próxima señal esperada. Esa estructura corta evita malentendidos y, sobre todo, reduce dependencia de personas concretas para mantener contexto.

Para que esto no quede en documento, conviene conectar la gobernanza con los pipelines. Si una migración está fuera de ventana o incumple gate acordado, el sistema de calidad debería advertirlo temprano. No para bloquear por bloquear, sino para evitar que la inconsistencia se descubra cuando ya hay usuarios afectados.

Cuando miras este enfoque en perspectiva, aparece una ventaja clara: el trimestre deja de ser una sucesión de incendios técnicos y se convierte en una secuencia de decisiones con criterio acumulativo. Cada equipo mantiene ritmo, pero el producto conserva coherencia.

Con esta lección cerramos la parte de Maestría orientada a evolución organizativa. En la siguiente vamos a consolidar todo el recorrido del curso en una guía de operación final: cómo preparar una defensa técnica sólida del proyecto Android, conectando arquitectura, rendimiento, calidad y decisiones de negocio sin caer en discurso abstracto.

<!-- auto-gapfix:layered-mermaid -->
## Diagrama de arquitectura por capas

```mermaid
flowchart LR
  subgraph CORE[Core / Domain]
    C1[Entity]
    C2[Rule]
  end

  subgraph APP[Application]
    A1[UseCase]
    A2[Port]
  end

  subgraph UI[Interface]
    U1[ViewModel]
    U2[Screen]
  end

  subgraph INFRA[Infrastructure]
    I1[RemoteDataSource]
    I2[LocalDataSource]
  end

  A1 --> C1
  A1 -.-> A2
  U1 -.o A1
  A1 --o U1
  A2 -.-> I1
  A2 -.-> I2
```

La lectura del diagrama sigue esta semantica:
1. `-->` dependencia directa en runtime.
2. `-.->` contrato o abstraccion.
3. `-.o` wiring o composicion.
4. `--o` salida o propagacion de resultado.
