# Plan de refuerzo integral del curso Android

Este plan convierte la revisión crítica en ejecución concreta. El objetivo no es rehacer el curso desde cero, sino reforzarlo donde más impacta para cerrar la brecha de equivalencia con iOS y, sobre todo, para que el alumno salga con señales reales de empleabilidad técnica.

La idea central es simple: todo el recorrido debe desembocar en un único producto vivo, y cada nivel debe aportar una versión verificable de ese producto. Ese producto es RuralGO FieldOps, definido en [`00-brief-ruralgo-fieldops.md`](../stack-my-architecture-android/05-proyecto-final/00-brief-ruralgo-fieldops.md), con rúbrica de cierre en [`01-rubrica-empleabilidad.md`](../stack-my-architecture-android/05-proyecto-final/01-rubrica-empleabilidad.md) y evidencias obligatorias en [`02-evidencias-obligatorias.md`](../stack-my-architecture-android/05-proyecto-final/02-evidencias-obligatorias.md).

## Qué se refuerza en cada nivel

En Nivel Cero no se cambia el foco de alfabetización técnica, pero sí se introduce una disciplina de evidencia desde el primer día. Cada mini proyecto debe cerrar con un registro breve de ejecución: qué se intentó, qué falló, cómo se corrigió y qué quedó funcionando. Ese hábito se vuelve estructural y acompaña todo el curso.

En Junior, los entregables dejan de sentirse como piezas aisladas. Cada módulo se conecta explícitamente con la versión v1.0 del proyecto final. El alumno ya no entrega “una feature cualquiera”, sino una parte concreta de FieldOps con estado, navegación y persistencia funcionando en conjunto.

En Midlevel, el objetivo es endurecer robustez técnica y trazabilidad. Aquí se exige v2.0 con sincronización offline-first, integración real de red + Room + DataStore, y primera línea seria de calidad automatizada en CI. Midlevel pasa a ser el punto donde el alumno demuestra que no solo construye, sino que integra sin romper.

En Senior, se activa la capa operativa. El proyecto se convierte en v3.0 con release controlado, rollback viable, runbook de incidentes y señales de salud que permitan decidir bajo presión. Este nivel deja de ser únicamente “arquitectura bonita” y se vuelve entrenamiento de sostenibilidad de producto.

En Maestría, el foco es gobernanza y evolución de largo plazo. FieldOps pasa a v4.0 con contratos internos versionados, reglas de dependencia más estrictas, criterios de cambio entre equipos y defensa técnica formal de decisiones con evidencia.

## Mejoras concretas por módulo y continuidad pedagógica

El refuerzo no obliga a reescribir todos los módulos. Obliga a insertar puentes pedagógicos claros donde antes había saltos. Cada introducción de nivel incorpora ahora una sección de “estado actual de FieldOps”, para que el alumno entienda qué hereda, qué mejora y qué valida en ese tramo.

En los módulos de arquitectura, testing, observabilidad y rendimiento se añade una cláusula de aplicación obligatoria sobre el proyecto final. Eso evita que la lección se consuma como teoría separada y garantiza transferencia inmediata a un caso real del curso.

En los módulos avanzados de Senior y Maestría, cada decisión técnica debe cerrar con una evidencia de impacto operativo. Ya no basta con explicar por qué una estrategia “suena correcta”; hay que mostrar qué señal la valida o la refuta.

## Criterios de evaluación reforzados

La evaluación deja de fragmentarse por “entregables sueltos” y se unifica en dos capas. La primera capa mide progreso por nivel sobre el producto vivo. La segunda capa mide readiness final con la rúbrica de empleabilidad de 100 puntos.

La aprobación final requiere superar el umbral global y no tener vacíos críticos en arquitectura, testing u operación. Este criterio protege al alumno de una falsa sensación de preparación basada en fortalezas parciales.

## Evidencias esperadas de aprendizaje

La evidencia mínima exigible en cada hito incluye código ejecutable, pruebas pasando, señal de calidad/rendimiento acorde al nivel, y defensa técnica escrita en lenguaje propio. Con esto se evalúa comprensión, ejecución y capacidad de explicar decisiones, que es lo que de verdad se pide en contexto profesional.

## Plan de implementación priorizado

La primera prioridad es estabilizar el marco del proyecto final transversal y enlazarlo desde los puntos de entrada del curso. Esto tiene el mayor impacto con el menor riesgo de ruptura curricular.

La segunda prioridad es adaptar entregables de Junior, Midlevel, Senior y Maestría para que validen explícitamente versiones sucesivas de FieldOps. Aquí se gana coherencia pedagógica de extremo a extremo.

La tercera prioridad es endurecer quality gates y evidencias de CI/rendimiento/publicación en el cierre final. Ese paso transforma la experiencia de “curso completo” en “preparación profesional defendible”.

La cuarta prioridad es ejecutar una auditoría final de equivalencia contra iOS con resultado explícito de brechas cerradas y pendientes residuales.

```kotlin
package com.stackmyarchitecture.reinforcement

data class ReinforcementMilestone(
    val name: String,
    val scope: String,
    val completionCriteria: String
)

class ReinforcementPlanner {
    fun orderedMilestones(): List<ReinforcementMilestone> {
        return listOf(
            ReinforcementMilestone(
                name = "Marco proyecto final",
                scope = "Definición transversal y enlaces curriculares",
                completionCriteria = "Brief, rúbrica y evidencias integrados"
            ),
            ReinforcementMilestone(
                name = "Alineación por nivel",
                scope = "Entregables Junior/Midlevel/Senior/Maestría sobre FieldOps",
                completionCriteria = "Cada nivel entrega versión verificable"
            ),
            ReinforcementMilestone(
                name = "Cierre operativo",
                scope = "CI, rendimiento, publicación y defensa técnica",
                completionCriteria = "Evidencia completa de empleabilidad"
            )
        )
    }
}
```

Este código no es decorativo. Resume la lógica de implementación: primero crear columna vertebral, luego conectar niveles, luego cerrar con evidencia operativa.

