# Nivel Maestría · 07 · Defensa técnica del proyecto Android

Llegar al final de un curso técnico no significa solo tener código funcionando. Significa poder explicar por qué ese código existe así y no de otra forma. Esa diferencia es importante porque, en el mundo real, las decisiones se aprueban cuando se entienden. Si no sabes defender lo que construiste, el sistema puede estar bien hecho y aun así perder credibilidad.

Esta lección está pensada para ese momento exacto. No vamos a preparar una presentación “bonita”. Vamos a preparar una conversación técnica sólida, de las que tienes con un lead, con un arquitecto o con un equipo de producto cuando hay que decidir si una arquitectura está lista para escalar.

La trampa más común en una defensa es contar solo componentes: “tenemos Hilt, Room, WorkManager, tests...”. Eso describe herramientas, pero no demuestra criterio. Lo que de verdad convence es conectar cada elección con un problema concreto. Elegimos Room porque necesitábamos continuidad de experiencia sin red estable. Elegimos WorkManager porque ciertas tareas debían sobrevivir reinicios y no podían depender de que la app siguiera abierta. Elegimos contratos internos porque varios equipos necesitaban evolucionar en paralelo sin romperse entre sí.

Cuando explicas así, la conversación cambia. Ya no suena a checklist de tecnologías. Suena a diseño orientado a contexto.

Para ayudarte a estructurar esa conversación de forma natural, conviene tener un “mapa mental de defensa” en código y en arquitectura. Por ejemplo, si alguien te pregunta cómo protegiste coherencia entre UI y datos en escenarios de latencia alta, puedes enseñar cómo el `ViewModel` no depende del framework de red y cómo el repositorio centraliza la estrategia offline-first.

```kotlin
package com.stackmyarchitecture.tasks.application

class ObserveTasksUseCase(
    private val repository: TasksRepository
) {
    fun execute(): kotlinx.coroutines.flow.Flow<List<TaskItem>> {
        return repository.observeTasks()
    }
}

interface TasksRepository {
    fun observeTasks(): kotlinx.coroutines.flow.Flow<List<TaskItem>>
    suspend fun refreshIfNeeded()
}

data class TaskItem(
    val id: String,
    val title: String,
    val completed: Boolean
)
```

Este fragmento parece simple, y justo por eso es potente para una defensa. Muestra que el caso de uso expresa intención del dominio y evita contaminarse con detalles de Retrofit, Room o DataStore. Esa separación no es estética. Te permite cambiar infraestructura sin romper comportamiento observable de la capa de aplicación.

Después suele aparecer una pregunta clave: cómo se comporta este diseño cuando algo falla en producción. Aquí es donde mucha gente se queda sin narrativa porque su arquitectura no está conectada con operación. En tu caso, sí lo está: puedes explicar que la app tiene telemetría para migraciones, quality gates en CI y estrategia de rollback, de modo que la fiabilidad no depende de heroicidad individual.

```kotlin
package com.stackmyarchitecture.core.reliability

data class ReliabilitySignal(
    val feature: String,
    val errorRate: Double,
    val p95LatencyMs: Long
)

interface ReliabilityEvaluator {
    fun isHealthy(signal: ReliabilitySignal): Boolean
}

class DefaultReliabilityEvaluator : ReliabilityEvaluator {
    override fun isHealthy(signal: ReliabilitySignal): Boolean {
        return signal.errorRate <= 0.01 && signal.p95LatencyMs <= 400
    }
}
```

Otra parte que marca diferencia en una defensa profesional es reconocer trade-offs sin ponerte a la defensiva. Si alguien te pregunta por qué mantuviste convivencia entre contratos `v1` y `v2`, la respuesta madura no es “porque era más fácil”. La respuesta madura es que priorizaste continuidad de entrega entre equipos, aceptando complejidad temporal y retirándola con una política explícita de sunset. Eso demuestra control del coste técnico a lo largo del tiempo.

También ayuda mucho hablar del impacto en personas, no solo en código. Una arquitectura buena no solo compila; reduce fricción de colaboración. Cuando delimitaste bounded contexts y ownership técnico, no solo ordenaste paquetes. Diste a cada equipo autonomía real para evolucionar su dominio sin arrastrar a todos en cada cambio.

En una entrevista o revisión interna, este punto suele ser decisivo porque conecta tecnología con productividad de organización.

Si quieres llevar esta defensa a nivel semisenior sólido, cuida especialmente el cierre de tu relato. No termines con “todo funciona”. Termina con qué evidencia te permite afirmar que funciona de forma sostenible. En tu proyecto, esa evidencia está en tests de UI y de integración, en métricas de rendimiento con Macrobenchmark y Baseline Profiles, en reglas de calidad en CI y en decisiones de arquitectura trazables.

Cuando presentas así, el mensaje final queda claro: no construiste una demo, construiste un sistema que puede evolucionar.

Con esta lección cerramos la secuencia principal de Maestría. Lo que sigue es aplicar este mismo criterio en tu proyecto final, defendiendo decisiones de manera honesta, técnica y conectada con el problema real de producto que quieres resolver.

---

## Ejercicio guiado

**Objetivo**: Preparar tres preguntas de defensa técnica sobre el proyecto Android y redactar una respuesta sólida para cada una, conectando decisiones de arquitectura con problemas reales de producto.

**Pasos**:
1. Formula la pregunta 1 sobre offline-first: ¿por qué la UI no depende de la red directamente y cómo garantizas consistencia de datos?
2. Formula la pregunta 2 sobre testabilidad: ¿cómo demuestras con pruebas que el flujo de sincronización funciona sin necesidad de una API real?
3. Formula la pregunta 3 sobre operación: ¿qué harías si en producción la tasa de error de sync supera el 5% durante un release?
4. Condición de éxito: cada respuesta menciona al menos una decisión de arquitectura concreta (clase, patrón o mecanismo) y su impacto observable en el producto o en el equipo.

<details>
<summary>Solución de referencia</summary>

```
Pregunta 1: ¿Por qué la UI no depende de la red directamente?

La UI observa siempre Room como fuente de verdad a través de `Flow<List<Task>>` expuesto
por el repositorio. La red solo actualiza el estado local; nunca hay una llamada directa
de la capa de presentación a Retrofit. Esto garantiza que el usuario ve datos coherentes
aunque esté sin conexión: las acciones se guardan con `SyncState.PENDING` y se sincronizan
cuando WorkManager detecta que la red vuelve. La consistencia se mantiene porque Room es
reactivo: cualquier cambio local emite automáticamente al flow.

---

Pregunta 2: ¿Cómo demuestras con pruebas que la sincronización funciona?

Usamos `FakeTasksDao` y `FakeTasksRemoteDataSource` en tests unitarios de
`TasksSyncOrchestrator`. El test prepara un DAO con tareas en estado `PENDING`, ejecuta
`syncPendingTasks()` con `advanceUntilIdle()` y verifica que el DAO actualiza las filas
a `SYNCED`. No se necesita emulador ni servidor real. La ausencia de dependencias externas
hace los tests repetibles en milisegundos en CI, lo que permite ejecutarlos en cada PR.

---

Pregunta 3: ¿Qué harías si la tasa de error de sync supera el 5% en producción?

1. Verificar en el tablero operativo si el aumento está concentrado en una versión o
   segmento concreto (API level, tipo de red).
2. Si está correlacionado con un release reciente: pausar expansión del rollout en Play Console.
3. Si el problema es el endpoint de sincronización: desactivar el flag que activa la nueva
   estrategia de sync (si existe) para reducir impacto sin rollback completo.
4. Si no mejora en 15 minutos: activar rollback y abrir postmortem siguiendo el runbook
   `docs/runbooks/incident-sync-failure.md`.
5. En paralelo, analizar logs estructurados con `operationId` para aislar la causa raíz
   antes de re-lanzar la corrección.
```

```kotlin
// Fragmento que ilustra la respuesta 2 en código
class FakeTasksSyncOrchestrator {
    var syncCalled = false
    var shouldFail = false

    suspend fun syncPendingTasks() {
        syncCalled = true
        if (shouldFail) throw IllegalStateException("Sync error simulado")
    }
}

// En el test:
// val fake = FakeTasksSyncOrchestrator()
// val repo = TasksRepository(dao = fakeDao, syncScheduler = fake, clock = { 1000L })
// repo.markTaskDoneOfflineFirst("task-1", current)
// assertTrue(fake.syncCalled)
```

**Resultado esperado**: las tres respuestas se pueden exponer verbalmente en 60–90 segundos cada una; quien escucha puede hacer preguntas de seguimiento sin que surjan inconsistencias; el código de ejemplo compila y es coherente con la arquitectura descrita en el curso.

</details>

<!-- auto-gapfix:layered-mermaid -->
## Diagrama de arquitectura por capas

```mermaid
flowchart LR
  subgraph CORE["Core / Domain"]
    direction TB
    ENT[Entity]
    POL[Policy]
  end

  subgraph APP["Application"]
    direction TB
    BOOT[Composition Root]
    UC[UseCase]
    PORT["FeaturePort (contrato)"]
  end

  subgraph UI["Interface"]
    direction TB
    VM[ViewModel]
    VIEW[View]
  end

  subgraph INFRA["Infrastructure"]
    direction TB
    API[API Client]
    STORE[Persistence Adapter]
  end

  VM --> UC
  UC --> ENT
  UC ==> PORT
  BOOT -.-> PORT
  BOOT -.-> API
  BOOT -.-> STORE
  PORT --o API
  PORT --o STORE
  UC --o VM

  style CORE fill:#0f2338,stroke:#63a4ff,color:#dbeafe,stroke-width:2px
  style APP fill:#2a1f15,stroke:#fb923c,color:#ffedd5,stroke-width:2px
  style UI fill:#14262f,stroke:#93c5fd,color:#e0f2fe,stroke-width:2px
  style INFRA fill:#2a1d34,stroke:#c084fc,color:#f3e8ff,stroke-width:2px

  linkStyle 0 stroke:#f472b6,stroke-width:2.6px
  linkStyle 1 stroke:#f472b6,stroke-width:2.6px
  linkStyle 2 stroke:#60a5fa,stroke-width:2.8px
  linkStyle 3 stroke:#94a3b8,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 4 stroke:#94a3b8,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 5 stroke:#94a3b8,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 6 stroke:#86efac,stroke-width:2.6px
  linkStyle 7 stroke:#86efac,stroke-width:2.6px
  linkStyle 8 stroke:#86efac,stroke-width:2.6px
```

La lectura del diagrama sigue esta semántica:
1. `-->` dependencia directa en runtime.
2. `-.->` wiring o configuración.
3. `==>` contrato o abstracción.
4. `--o` salida o propagación de resultado.
