# Mejoras por módulo, criterios y evidencias

Este documento baja el plan de refuerzo a nivel de ejecución curricular. No sustituye las lecciones existentes. Las conecta con una exigencia común: cada módulo debe dejar una mejora concreta sobre RuralGO FieldOps y una evidencia verificable de aprendizaje.

## Nivel Cero

En este nivel se mantiene la prioridad de comprensión base, pero se incorpora una mejora estructural en todos los módulos: cada práctica termina con un registro mínimo de evidencia. Ese registro debe incluir captura de ejecución, error principal encontrado y corrección aplicada. El objetivo no es producir software grande, sino instalar una disciplina de aprendizaje observable desde el inicio.

El criterio de evaluación aquí es claridad de comprensión y capacidad de corregir errores frecuentes sin bloqueo total. La evidencia esperada es una mini app navegable y una bitácora breve de decisiones.

## Junior

La mejora principal de Junior es dejar de tratar los entregables como piezas independientes. Cada módulo aporta una parte explícita de la versión v1.0 de FieldOps. El alumno debe entender que arquitectura, estado, navegación, persistencia y pruebas forman parte del mismo sistema, no de cinco ejercicios distintos.

El criterio de evaluación es integración funcional básica con separación de responsabilidades. La evidencia esperada es un flujo usable de dos o más pantallas, ViewModel por pantalla, persistencia local coherente y pruebas mínimas pasando.

## Midlevel

La mejora principal de Midlevel es endurecer robustez y trazabilidad técnica en v2.0 de FieldOps. Cada módulo debe conectarse con problemas reales de sincronización, red inestable y consistencia de datos.

El criterio de evaluación es que el sistema se mantenga operativo bajo condiciones no ideales. La evidencia esperada es sincronización offline-first funcional, pruebas de integración sobre flujos críticos y señales mínimas de calidad en CI.

## Senior

La mejora principal de Senior es convertir la app en un producto operable, no solo implementable. Aquí la versión v3.0 debe demostrar estrategia de release, rollback y respuesta a incidentes con criterio técnico.

El criterio de evaluación es capacidad de sostener cambios bajo presión sin degradar estabilidad de forma ciega. La evidencia esperada es runbook operativo, decisiones de priorización con señales y validación de salud del sistema tras release.

## Maestría

La mejora principal de Maestría es gobernanza de evolución en v4.0. Los módulos deben consolidar contratos versionados, reglas de dependencia y defensa técnica de decisiones con impacto organizativo real.

El criterio de evaluación es madurez para liderar decisiones de arquitectura y evolución multi-equipo con evidencia. La evidencia esperada es defensa técnica estructurada, trazabilidad de cambios y cierre profesional de publicación/mantenimiento.

## Puente transversal obligatorio

Todos los niveles deben referenciar explícitamente el estado de FieldOps al inicio de cada introducción de bloque. Esto elimina saltos pedagógicos y deja claro qué hereda el alumno, qué mejora en el nivel actual y qué evidencia debe producir para avanzar.

```kotlin
package com.stackmyarchitecture.curriculum

data class ModuleReinforcement(
    val level: String,
    val targetVersion: String,
    val expectedEvidence: String
)

class CurriculumContinuityChecker {
    fun hasContinuity(reinforcement: ModuleReinforcement): Boolean {
        return reinforcement.level.isNotBlank() &&
            reinforcement.targetVersion.isNotBlank() &&
            reinforcement.expectedEvidence.isNotBlank()
    }
}
```

Este bloque de código representa el contrato pedagógico reforzado: cada módulo debe decir qué versión del producto toca y qué evidencia deja. Si eso no está claro, la continuidad se rompe.

