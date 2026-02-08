# Informe del curso

## Resumen ejecutivo

Este curso está diseñado para una persona de 14 años sin experiencia previa en programación. La ruta avanza desde Nivel Cero hasta Maestría con aprendizaje progresivo, práctica constante y evidencias claras de progreso.

## Estándar pedagógico obligatorio de redacción

Desde este punto del curso, toda lección debe escribirse como una explicación docente completa y guiada, no como una chuleta ni como un resumen corto. Esto significa que el contenido principal debe ir en formato narrativo paso a paso, con frases que conecten cada idea con la anterior y con un lenguaje claro para alguien que empieza desde cero. Cada término técnico tiene que definirse antes de usarse, y cada concepto nuevo debe explicar qué es, por qué importa, cómo se utiliza y para qué sirve en una situación real.

También significa que, en el cuerpo principal de cada lección, no se deben usar listas con viñetas para sustituir la explicación. Las listas solo se aceptan en zonas de apoyo, como una rúbrica de evaluación o un checklist final, pero no como forma principal de enseñar el tema. Si una lección incluye código, el texto debe preparar primero al estudiante explicando línea por línea qué va a leer. Después del bloque de código, el texto debe volver a explicar qué ocurrió, qué resultado se espera y qué error típico puede aparecer en ese punto.

El tono de todo el curso debe ser cercano, paciente y riguroso. Cercano para reducir miedo, paciente para anticipar dudas y riguroso para no simplificar de forma incorrecta. Queda prohibido asumir conocimientos no enseñados en lecciones anteriores. Si un módulo necesita una base que aún no se explicó, el módulo debe introducir esa base antes de continuar.

Por último, cada lección debe cerrar con una comprobación de comprensión y con una evidencia concreta de progreso. Esa evidencia debe ser verificable, por ejemplo un ejercicio resuelto, una salida de código o una explicación escrita por el estudiante.

Este estándar debe mantener un patrón pedagógico estable, profundo y progresivo en todo el curso Android. Eso implica continuidad entre secciones, explicación incremental sin saltos mentales y conexión explícita de cada decisión con el módulo arquitectónico correspondiente.

Cuando aparezca una palabra clave, anotación o patrón de Android o Kotlin, su definición debe darse en el mismo punto donde aparece por primera vez. Si en una lección se usa un término como Composable, data class, sealed interface, HiltAndroidApp, ViewModel, Repository o cualquier equivalente técnico, el texto debe explicar de inmediato qué significa, por qué se usa ahí y qué impacto tendría no usarlo.

En las lecciones que incorporen arquitectura, la introducción de Clean Architecture, DDD y feature-first debe ser gradual y en el momento correcto del plan formativo. No se permite adelantar conceptos de etapas superiores ni tratarlos de forma superficial.

Para reforzar control de calidad pedagógica, cada revisión de módulo debe comprobar cuatro criterios obligatorios. El primero exige narración continua sin reemplazar explicación por listas. El segundo exige explicación línea por línea de los bloques de código relevantes. El tercero exige definición inmediata de términos nuevos. El cuarto exige trazabilidad didáctica, es decir, conectar lo nuevo con lo aprendido antes y con la capa arquitectónica actual.

## Perfil de entrada

- Edad orientativa: 14 años
- Sin conocimientos previos de programación
- Sin experiencia con terminal, Android Studio, Git ni arquitectura

## Perfil de salida

Al finalizar, el estudiante puede construir y mantener apps Android reales con stack moderno, arquitectura clara, pruebas y criterios de calidad profesionales.

## Principios didácticos obligatorios

1. Explicar simple antes de profundizar.
2. Un concepto nuevo importante por bloque.
3. Ejemplo mínimo antes de ejemplo real.
4. Práctica guiada en todas las lecciones.
5. Mini reto en todas las lecciones.
6. Corrección explícita de errores comunes.
7. Evidencias medibles para avanzar de nivel.

## Matriz técnica validada

| Componente | Versión | Fuente oficial |
|---|---:|---|
| Kotlin | 2.3.10 | https://kotlinlang.org/docs/releases.html |
| Android Gradle Plugin | 9.0.0 | https://developer.android.com/build/releases/agp-9-0-0-release-notes |
| Gradle | 9.1.0 | https://developer.android.com/build/releases/agp-9-0-0-release-notes |
| JDK | 17 | https://developer.android.com/build/releases/agp-9-0-0-release-notes |
| compileSdk / targetSdk | 36 | https://developer.android.com/about/versions/16/setup-sdk |
| Compose BOM | 2026.01.01 | https://developer.android.com/develop/ui/compose/bom |
| Navigation Compose | 2.9.6 | https://developer.android.com/develop/ui/compose/navigation |

## Sistema de evaluación

- Evaluación diagnóstica al iniciar nivel.
- Evaluación formativa por módulo.
- Evaluación sumativa por proyecto integrador.
- Hito de paso de nivel con rúbrica obligatoria.

## Evidencias obligatorias por nivel

- Código funcional.
- Evidencia de ejecución.
- Mini retos resueltos.
- Checklist del nivel completado.
- Bitácora breve de aprendizaje.

## Métricas de éxito del curso

1. Tasa de finalización por nivel.
2. % de mini retos superados sin ayuda externa.
3. % de proyectos integradores entregados y aprobados.
4. Tiempo promedio de corrección de errores clave.

## Riesgos pedagógicos y mitigaciones

- Sobrecarga cognitiva: dividir en microbloques y recapitulaciones.
- Frustración por errores: guías de depuración paso a paso.
- Saltos de dificultad: gate de evidencias antes de avanzar.
- Dependencias técnicas cambiantes: política de actualización de matriz.
