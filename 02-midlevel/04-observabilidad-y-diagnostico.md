# Nivel Midlevel · 04 · Observabilidad y diagnóstico en Android, sin adivinar errores

En los módulos anteriores ya construiste una base potente. Tienes red robusta, sincronización offline-first y reglas de consistencia. Ahora aparece un problema nuevo que siempre llega cuando una app empieza a crecer. El problema ya no es “cómo programar una feature”. El problema es “cómo saber qué está pasando cuando falla en producción”.

Ese es exactamente el objetivo de este módulo. Vamos a construir observabilidad básica pero profesional para Android. Observabilidad significa que el sistema deja huellas útiles para entender comportamiento, detectar fallos y diagnosticar causas sin improvisar.

Aquí no vamos a meter una plataforma externa compleja todavía. Vamos a trabajar primero con base nativa de Android para que entiendas el fundamento técnico.

---

## 1) Qué es observabilidad y por qué importa aquí

En Android, muchas incidencias no se reproducen fácil en desarrollo. Pueden depender de red, batería, estado del dispositivo, permisos o secuencia de eventos.

Si no tienes observabilidad, cuando aparece un bug solo puedes decir “a mí no me pasa”. Eso no escala.

Si sí tienes observabilidad, puedes responder preguntas concretas. Qué acción se estaba ejecutando, en qué capa falló, con qué tipo de error y qué decisión tomó la app después.

En términos de arquitectura, observabilidad no debe vivir solo en UI. Debe cruzar repositorio, orquestador y trabajos de sincronización, porque ahí es donde pasan las decisiones críticas que ya implementaste en módulos Midlevel 01, 02 y 03.

---

## 2) Definiciones mínimas antes de código

Un log estructurado es un registro con campos claros, no solo un texto suelto. Ejemplo: evento, módulo, entidad, resultado.

Un nivel de log es la severidad del mensaje. En este módulo usaremos DEBUG, INFO, WARN y ERROR.

Correlación significa poder seguir una misma operación a través de varias capas usando un identificador común, por ejemplo un `operationId`.

Diagnóstico es el proceso de reconstruir qué pasó, en qué orden y por qué.

Con estos términos claros, pasamos a construir la base.

---

## 3) Crear contrato de logging para no acoplar capas

Primero definimos una interfaz de logging en lugar de llamar APIs directas desde cualquier clase.

```kotlin
interface AppLogger {
    fun d(tag: String, message: String, metadata: Map<String, String> = emptyMap())
    fun i(tag: String, message: String, metadata: Map<String, String> = emptyMap())
    fun w(tag: String, message: String, metadata: Map<String, String> = emptyMap())
    fun e(tag: String, message: String, throwable: Throwable? = null, metadata: Map<String, String> = emptyMap())
}
```

Explicación línea por línea:

Línea `interface AppLogger` define un contrato. La arquitectura gana porque cualquier capa depende de interfaz, no de implementación concreta.

Línea `fun d(...)` define método para eventos de depuración.

Línea `tag: String` identifica origen del log, por ejemplo `TasksRepository`.

Línea `message: String` contiene descripción breve del evento.

Línea `metadata: Map<String, String> = emptyMap()` añade campos estructurados opcionales sin obligar siempre a enviarlos.

Línea `fun i(...)` define nivel informativo.

Línea `fun w(...)` define advertencias que no rompen flujo pero sí merecen atención.

Línea `fun e(...)` define errores.

Línea `throwable: Throwable? = null` permite adjuntar excepción real cuando exista.

Por qué se usa aquí: unifica formato de logs y evita código disperso.

Qué pasaría si no se usa: cada clase loguearía distinto y el diagnóstico sería caótico.

---

## 4) Implementación Android con Logcat

Ahora implementamos el contrato usando `android.util.Log`.

```kotlin
class AndroidAppLogger : AppLogger {

    override fun d(tag: String, message: String, metadata: Map<String, String>) {
        Log.d(tag, format(message, metadata))
    }

    override fun i(tag: String, message: String, metadata: Map<String, String>) {
        Log.i(tag, format(message, metadata))
    }

    override fun w(tag: String, message: String, metadata: Map<String, String>) {
        Log.w(tag, format(message, metadata))
    }

    override fun e(tag: String, message: String, throwable: Throwable?, metadata: Map<String, String>) {
        Log.e(tag, format(message, metadata), throwable)
    }

    private fun format(message: String, metadata: Map<String, String>): String {
        if (metadata.isEmpty()) return message
        val fields = metadata.entries.joinToString(separator = " ") { (k, v) -> "$k=$v" }
        return "$message | $fields"
    }
}
```

Explicación línea por línea:

Línea `class AndroidAppLogger : AppLogger` crea implementación concreta para Android.

Línea `override fun d(...)` implementa nivel debug.

Línea `Log.d(tag, format(message, metadata))` escribe en Logcat con mensaje ya estructurado.

Bloques `i`, `w` y `e` repiten el mismo patrón para cada severidad.

Línea `Log.e(..., throwable)` adjunta stacktrace cuando hay excepción.

Línea `private fun format(...)` centraliza formato de salida.

Línea `if (metadata.isEmpty()) return message` evita añadir separadores innecesarios.

Línea `joinToString` convierte mapa en pares `clave=valor` legibles.

Línea `return "$message | $fields"` produce salida final estable.

Por qué se usa aquí: estandariza logs y hace más fácil filtrar en diagnóstico.

Qué pasaría si formateas en cada clase: inconsistencias y más trabajo al investigar fallos.

---

## 5) Inyectar logger con Hilt para usarlo en todas las capas

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object ObservabilityModule {

    @Provides
    @Singleton
    fun provideAppLogger(): AppLogger {
        return AndroidAppLogger()
    }
}
```

Explicación línea por línea:

Línea `@Module` marca clase de proveedores para Hilt.

Línea `@InstallIn(SingletonComponent::class)` indica que el binding vive en el grafo singleton de app.

Línea `object ObservabilityModule` crea módulo singleton de Kotlin.

Línea `@Provides` indica función proveedora de dependencia.

Línea `@Singleton` garantiza una sola instancia de logger para toda la app.

Línea `fun provideAppLogger(): AppLogger` define que se inyectará por interfaz.

Línea `return AndroidAppLogger()` construye implementación concreta.

Por qué se usa aquí: desacopla consumo de logs respecto a implementación.

Qué pasaría si no usas DI: difícil testear y reemplazar logger por doubles en pruebas.

---

## 6) Registrar eventos en repositorio y orquestador

Ahora aplicamos observabilidad donde realmente importa, no solo en UI.

```kotlin
class TasksRepository(
    private val dao: TasksDao,
    private val syncScheduler: SyncScheduler,
    private val logger: AppLogger,
    private val clock: () -> Long
) {
    suspend fun markTaskDoneOfflineFirst(taskId: String, current: TaskEntity) {
        val operationId = "task_done_${clock()}"

        logger.i(
            tag = "TasksRepository",
            message = "Inicio de actualizacion offline-first",
            metadata = mapOf("operationId" to operationId, "taskId" to taskId)
        )

        val updated = current.copy(done = true, updatedAtMillis = clock(), syncState = SyncState.PENDING)
        dao.update(updated)
        syncScheduler.scheduleOneTimeSync()

        logger.i(
            tag = "TasksRepository",
            message = "Actualizacion local completada y sync programado",
            metadata = mapOf("operationId" to operationId, "taskId" to taskId, "syncState" to "PENDING")
        )
    }
}
```

Explicación línea por línea:

Línea `private val logger: AppLogger` añade logger al repositorio por DI.

Línea `val operationId = "task_done_${clock()}"` crea correlación para seguir esta operación de punta a punta.

Primer bloque `logger.i(...)` registra inicio de operación con metadatos clave.

Línea `val updated = current.copy(...)` aplica cambio local offline-first.

Línea `dao.update(updated)` persiste en Room.

Línea `syncScheduler.scheduleOneTimeSync()` programa sincronización.

Segundo bloque `logger.i(...)` registra final del tramo local, dejando rastro de estado.

Por qué se usa aquí: si algo falla después, puedes reconstruir secuencia y contexto.

Qué pasaría sin `operationId`: sería mucho más difícil vincular logs de una misma acción.

---

## 7) Registrar errores de forma útil, no ruidosa

```kotlin
suspend fun syncPendingTasks() {
    try {
        // flujo de sync
    } catch (t: Throwable) {
        logger.e(
            tag = "TasksSyncOrchestrator",
            message = "Fallo durante sincronizacion de pendientes",
            throwable = t,
            metadata = mapOf("phase" to "syncPendingTasks")
        )
        throw t
    }
}
```

Explicación línea por línea:

Línea `try {` envuelve tramo crítico.

Línea `catch (t: Throwable)` captura error inesperado.

Bloque `logger.e(...)` registra error con contexto y excepción original.

Línea `throw t` relanza para no esconder fallo al flujo superior.

Por qué se usa aquí: loguear no debe tragarse errores.

Qué pasaría si no relanzas: podrías ocultar fallos y dejar estados inconsistentes silenciosos.

---

## 8) Mapear eventos de dominio técnico a señales de diagnóstico

Cuando un conflicto se resuelve, debes dejar evidencia de la decisión.

```kotlin
logger.i(
    tag = "ConflictResolver",
    message = "Decision de conflicto aplicada",
    metadata = mapOf(
        "taskId" to local.id,
        "resolution" to "KEEP_REMOTE",
        "localUpdatedAt" to local.updatedAtMillis.toString(),
        "remoteUpdatedAt" to remote.updatedAtMillis.toString()
    )
)
```

Explicación línea por línea:

Línea `tag = "ConflictResolver"` identifica módulo responsable.

Línea `message = "Decision de conflicto aplicada"` describe evento estable para búsquedas.

Bloque `metadata = mapOf(...)` agrega campos concretos para auditoría técnica.

Línea `"resolution" to "KEEP_REMOTE"` deja claro qué camino se tomó.

Líneas de timestamps permiten verificar por qué ganó esa rama.

Por qué se usa aquí: evita decisiones opacas en conflictos.

Qué pasaría sin esto: no podrías explicar al usuario o al equipo por qué cambió un dato.

---

## 9) Pruebas mínimas de observabilidad

No basta con decir “logea”. También se prueba.

```kotlin
class FakeLogger : AppLogger {
    val entries = mutableListOf<String>()

    override fun d(tag: String, message: String, metadata: Map<String, String>) {
        entries.add("D|$tag|$message|$metadata")
    }

    override fun i(tag: String, message: String, metadata: Map<String, String>) {
        entries.add("I|$tag|$message|$metadata")
    }

    override fun w(tag: String, message: String, metadata: Map<String, String>) {
        entries.add("W|$tag|$message|$metadata")
    }

    override fun e(tag: String, message: String, throwable: Throwable?, metadata: Map<String, String>) {
        entries.add("E|$tag|$message|$metadata|${throwable?.javaClass?.simpleName}")
    }
}
```

Explicación línea por línea:

Línea `class FakeLogger : AppLogger` crea doble de prueba que implementa el mismo contrato.

Línea `val entries = mutableListOf<String>()` almacena logs capturados para assertions.

Cada override añade una entrada en formato simple y verificable.

La línea de `e(...)` también incluye el tipo de excepción para validar trazabilidad de errores.

Por qué se usa aquí: pruebas de observabilidad sin depender de Logcat real.

Qué pasaría sin fake: sería difícil afirmar en tests qué se registró.

---

## 10) Conexión con arquitectura y siguientes módulos

Con este módulo, observabilidad queda integrada como capacidad transversal en Android sin romper separación de capas.

Repositorio y orquestador registran eventos técnicos. UI se mantiene limpia. Logger se inyecta por interfaz y se reemplaza en tests. Esa estructura prepara el terreno para quality gates y diagnóstico avanzado de bloques Senior.

---

## 11) Errores frecuentes en observabilidad

Error uno. Loguear textos genéricos sin metadatos. Luego no puedes filtrar ni correlacionar.

Error dos. Loguear todo como ERROR. Eso crea ruido y quita utilidad operacional.

Error tres. Hacer logs de datos sensibles. Nunca registres tokens o información privada.

Error cuatro. Loguear en UI y olvidar capas de negocio/infraestructura donde nace el problema real.

---

## 12) Mini reto final

Añade observabilidad completa al flujo `markTaskDoneOfflineFirst`.

Primero registra inicio con `operationId`.

Después registra fin de escritura local con `syncState`.

Luego provoca un fallo controlado en sincronización y valida en test que existe una entrada `ERROR` con `phase=syncPendingTasks`.

Si puedes mostrar esos tres registros en orden con el mismo `operationId`, ya tienes diagnóstico trazable de extremo a extremo.

