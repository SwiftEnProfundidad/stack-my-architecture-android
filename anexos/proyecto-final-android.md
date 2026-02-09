# Proyecto final Android · Guía de ejecución real

Si has llegado hasta aquí, ya no necesitas una lista de tareas para “hacer una app bonita”. Lo que necesitas es una guía para convertir todo lo aprendido en un producto que puedas defender, publicar y mantener sin que cada cambio se vuelva una fuente de estrés. Este anexo existe para eso.

La idea del proyecto final no es demostrar que sabes usar muchas librerías. La idea es demostrar que sabes resolver un problema real de principio a fin. Eso incluye diseño de dominio, arquitectura, decisiones de persistencia, estrategia de sincronización, calidad, rendimiento, release y operación. Si una pieza falta, el resultado puede parecer completo, pero no será sostenible.

Un buen punto de partida es elegir un problema cotidiano que tenga fricción real. Puede ser gestión de tareas, planificación de hábitos, seguimiento de gastos o catálogo personal de estudio. Lo importante es que el problema te obligue a tomar decisiones, no solo a pintar pantallas.

Cuando el alcance está bien planteado, el diseño empieza a ordenarse solo. Una feature para crear y editar entidades. Otra para listar y filtrar. Otra para detalle y acciones críticas. A partir de ahí, la arquitectura recomendada de Android deja de ser teoría y se convierte en una herramienta para no mezclar responsabilidades.

```kotlin
package com.stackmyarchitecture.finalproject.domain

data class HabitItem(
    val id: String,
    val title: String,
    val frequencyPerWeek: Int,
    val isArchived: Boolean
)

interface HabitRepository {
    fun observeHabits(): kotlinx.coroutines.flow.Flow<List<HabitItem>>
    suspend fun upsert(habit: HabitItem)
    suspend fun archive(id: String)
    suspend fun refreshIfNeeded()
}
```

Este tipo de contrato en dominio resuelve un problema clave: te permite construir la app alrededor del comportamiento que necesitas, no alrededor de la herramienta que uses debajo. Si mañana cambias parte de red o de base local, tu caso de uso sigue siendo legible y testeable.

En la capa de presentación, el proyecto final debería reflejar una UDF limpia y predecible. Eso significa que la UI emite intención, el ViewModel decide y el estado vuelve a la UI. Parece simple, pero en producción es la diferencia entre depurar minutos o depurar horas.

```kotlin
package com.stackmyarchitecture.finalproject.presentation

data class HabitUiState(
    val isLoading: Boolean = false,
    val items: List<HabitItem> = emptyList(),
    val message: String? = null
)

sealed interface HabitUiEvent {
    data object Refresh : HabitUiEvent
    data class Archive(val id: String) : HabitUiEvent
}
```

Cuando expliques este diseño en tu defensa final, no te quedes en “así se hace”. Cuenta qué problema evita. Evita efectos laterales invisibles entre UI y datos. Evita lógica dispersa en composables. Evita que cada interacción cree reglas implícitas difíciles de mantener.

En el apartado offline-first, el criterio profesional aparece en cómo priorizas experiencia de usuario. Si la app se queda sin red, el usuario no debería sentir que “todo murió”. Debería ver su información local y recibir sincronización cuando corresponda. Esa continuidad vale más que cualquier animación sofisticada.

El proyecto final también se evalúa por disciplina de calidad. Si tienes tests unitarios pero ninguna prueba de integración de flujos críticos, estás validando piezas aisladas, no comportamiento real. Si tienes benchmark pero no una decisión asociada a esas métricas, mediste sin gobernar. La calidad no es acumular herramientas; es cerrar el ciclo entre señal y decisión.

En publicación ocurre algo parecido. No basta con generar un `.aab` y subirlo. Necesitas coherencia entre versión, cambios publicados, salud operativa y plan de rollback. Cuando un reviewer te pregunte cómo gestionas riesgos en release, tu respuesta debe reflejar práctica, no intención.

```kotlin
android {
    defaultConfig {
        applicationId = "com.stackmyarchitecture.finalproject"
        versionCode = 1
        versionName = "1.0.0"
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
        }
    }
}
```

Ese bloque no cierra una app por sí solo, pero sí marca una postura: estás pensando en distribución real, tamaño, seguridad básica y trazabilidad de versión desde el inicio.

Si quieres saber si tu proyecto final está listo, hazte una pregunta simple y exigente a la vez. Si mañana otra persona entra al código, ¿podría entender por qué tomaste cada decisión sin preguntarte todo por chat? Si la respuesta es sí, has construido algo profesional.

Este anexo cierra el curso con una idea que vale para cualquier stack: la arquitectura no es el dibujo inicial, es la calidad de las decisiones que sostienes cuando el sistema cambia.
