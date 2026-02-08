# Nivel Midlevel · 08 · Observabilidad en producción: métricas y alertas que te avisan antes del usuario

Cuando una app falla en local, duele poco. La arreglas, vuelves a correr y sigues. El problema real empieza cuando falla en producción, porque ahí no ves la pantalla del usuario, no controlas su red, no controlas su batería y, casi siempre, el error llega incompleto. Te dicen “la app va mal” y con eso tienes que reconstruir qué pasó.

Por eso este módulo llega ahora. Ya blindaste bastante bien el desarrollo con pruebas de integración y quality gates. Incluso ya añadiste medición de rendimiento en CI. El siguiente salto natural es cerrar el hueco que más caro sale en equipos reales: saber qué está pasando de verdad cuando la app ya está publicada.

Aquí no vamos a hacer magia ni a llenar el proyecto de herramientas por moda. Vamos a construir una base de observabilidad de producción con propósito: métricas útiles, señales accionables y alertas que te obliguen a reaccionar cuando realmente importa.

---

## Qué problema resolvemos exactamente

Imagina que, después de una release, sube la tasa de errores en sincronización offline. Si no tienes observabilidad, te enteras tarde y mal. Primero llega soporte. Luego llegan reseñas negativas. Después alguien intenta reproducir a ciegas con logs locales que no representan el escenario real. Se pierde tiempo, confianza y foco.

Con observabilidad bien pensada, el flujo cambia por completo. La app emite señales cuando entra en estados críticos, esas señales se agregan como métricas y el sistema dispara alertas cuando una tendencia cruza el umbral que definiste. En lugar de perseguir humo, atacas un hecho medible.

---

## Qué vamos a instrumentar en este punto del roadmap

En este momento no necesitas vigilarlo todo. Necesitas vigilar lo que mueve riesgo de producto en lo que ya construiste durante Midlevel. Eso significa que vamos a observar la salud del sync offline-first, la estabilidad de pantallas críticas y la latencia de rutas donde el usuario siente fricción.

Este enfoque evita el error clásico de registrar miles de eventos inútiles. El objetivo no es generar ruido. El objetivo es tener pocas señales, pero con valor diagnóstico real.

---

## Crear una fachada de telemetría para no acoplar negocio a proveedor

Antes de elegir plataforma concreta, conviene proteger arquitectura. Si metes llamadas directas a SDK en cualquier ViewModel o repositorio, después migrar o cambiar estrategia se vuelve doloroso. La solución elegante es introducir un contrato propio.

```kotlin
interface Telemetry {
    fun trackEvent(name: String, attributes: Map<String, String> = emptyMap())
    fun trackMetric(name: String, value: Double, attributes: Map<String, String> = emptyMap())
    fun trackError(name: String, throwable: Throwable, attributes: Map<String, String> = emptyMap())
}
```

Este contrato parece simple, pero resuelve un problema de fondo. `trackEvent` te cubre hechos discretos, como “sync_started” o “sync_completed”. `trackMetric` te permite enviar valores numéricos agregables, por ejemplo duración de sync o ratio de éxito. `trackError` concentra la notificación de fallos con contexto homogéneo.

La decisión clave aquí es que las capas de negocio dependen de `Telemetry`, no de Firebase ni de ningún proveedor específico. Eso mantiene el diseño limpio y te deja espacio para evolucionar sin reescribir media app.

---

## Implementación inicial con Firebase Crashlytics y Analytics

Para producción Android, una base práctica y estable es combinar Crashlytics para errores y Firebase Analytics para eventos. Puedes evolucionar luego a OpenTelemetry o backend propio, pero para este punto del curso lo importante es resolver el problema real con algo que puedas operar ya.

```kotlin
class FirebaseTelemetry(
    private val analytics: FirebaseAnalytics,
    private val crashlytics: FirebaseCrashlytics
) : Telemetry {

    override fun trackEvent(name: String, attributes: Map<String, String>) {
        val bundle = Bundle().apply {
            attributes.forEach { (k, v) -> putString(k, v) }
        }
        analytics.logEvent(name, bundle)
    }

    override fun trackMetric(name: String, value: Double, attributes: Map<String, String>) {
        val bundle = Bundle().apply {
            putDouble("value", value)
            attributes.forEach { (k, v) -> putString(k, v) }
        }
        analytics.logEvent(name, bundle)
    }

    override fun trackError(name: String, throwable: Throwable, attributes: Map<String, String>) {
        attributes.forEach { (k, v) -> crashlytics.setCustomKey(k, v) }
        crashlytics.setCustomKey("error_name", name)
        crashlytics.recordException(throwable)
    }
}
```

Aquí cada decisión está conectada con un problema operativo. Transformar atributos a `Bundle` te permite consultar eventos desde paneles sin inventar parseos raros. En errores, fijar `customKey` evita reportes anónimos imposibles de agrupar por contexto. Cuando mañana te pregunten “qué versión o qué fase del sync falló”, ya tendrás esa información en el propio incidente.

No necesitas instrumentar cuarenta campos. Necesitas los campos que explican el incidente.

---

## Inyectar telemetría con Hilt para usarla en casos críticos

Con el contrato y la implementación listos, toca inyección para que no aparezcan singletons ocultos en cualquier clase.

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object TelemetryModule {

    @Provides
    @Singleton
    fun provideTelemetry(
        analytics: FirebaseAnalytics,
        crashlytics: FirebaseCrashlytics
    ): Telemetry = FirebaseTelemetry(analytics, crashlytics)
}
```

El porqué es directo. Si mañana quieres cambiar proveedor, crear una implementación dual o apagar telemetría en builds internas, solo tocas este borde de infraestructura. El resto del sistema sigue limpio.

---

## Instrumentar el flujo offline-sync donde realmente duele

Ahora lo importante: llevar telemetría a los puntos de riesgo que ya conoces por módulos anteriores. Empezamos por orquestación de sync.

```kotlin
class TasksSyncOrchestrator(
    private val tasksDao: TasksDao,
    private val api: TasksApi,
    private val telemetry: Telemetry,
    private val clock: () -> Long
) {

    suspend fun syncPendingTasks() {
        val startedAt = clock()
        telemetry.trackEvent("sync_started")

        try {
            val pending = tasksDao.getPending()
            api.syncPendingTasks(pending.map { it.toPayload() })
            tasksDao.markAllSynced(pending.map { it.id })

            val durationMs = (clock() - startedAt).toDouble()
            telemetry.trackMetric(
                name = "sync_duration_ms",
                value = durationMs,
                attributes = mapOf("result" to "success", "items" to pending.size.toString())
            )
            telemetry.trackEvent("sync_completed", mapOf("items" to pending.size.toString()))
        } catch (t: Throwable) {
            val durationMs = (clock() - startedAt).toDouble()
            telemetry.trackMetric(
                name = "sync_duration_ms",
                value = durationMs,
                attributes = mapOf("result" to "error")
            )
            telemetry.trackError(
                name = "sync_failed",
                throwable = t,
                attributes = mapOf("phase" to "syncPendingTasks")
            )
            throw t
        }
    }
}
```

Fíjate en la intención. No estamos metiendo telemetría por decorar, la estamos atando a decisiones críticas del flujo. Marcamos inicio para saber frecuencia real de intentos. Medimos duración para identificar degradaciones de latencia con el paso de releases. Distinguimos éxito de error para construir ratio de fiabilidad. Y cuando hay excepción, la enviamos con fase de contexto para no quedarnos en “IOException” genérico.

Este tipo de instrumentación te da respuestas accionables cuando algo se rompe: cuánto falló, cuándo empezó a fallar, cuánto tardaba antes y cuánto tarda ahora.

---

## Definir alertas pensando en impacto, no en ego técnico

Una alerta buena no es la que más suena. Es la que te despierta solo cuando hay riesgo real para usuario o negocio. Con lo que acabas de instrumentar, la primera alerta sensata es ratio de error de sync en ventana corta, por ejemplo 15 minutos, comparada con línea base reciente.

Otra alerta útil es incremento anómalo de duración media de `sync_duration_ms`. No porque “la métrica está fea”, sino porque ese síntoma suele preceder a timeouts, batería alta o experiencia errática en reconexión.

Si alertas por cada error individual, el equipo dejará de confiar en el sistema. Si alertas por tendencia con umbrales razonables, el sistema se convierte en copiloto real.

---

## Diferenciar señal de desarrollo y señal de producción

No todas las señales valen igual en todos los entornos. En debug quieres mucho detalle para investigar rápido. En producción quieres datos útiles sin exponer información sensible ni generar coste inútil.

Por eso conviene filtrar atributos sensibles y reducir cardinalidad de eventos. Si usas IDs únicos en cada evento de producción, destruyes agregación y disparas ruido. Es mejor agrupar por categorías estables que ayuden a ver tendencia.

Observabilidad madura no es “mandar todo”. Es mandar lo necesario para decidir bien.

---

## Probar que la instrumentación funciona sin esperar a prod

Antes de confiar en estas señales, valida en local con una implementación fake de `Telemetry` y tests de integración que comprueben emisión esperada en éxito y error.

```kotlin
class FakeTelemetry : Telemetry {
    val events = mutableListOf<String>()
    val metrics = mutableListOf<Pair<String, Double>>()
    val errors = mutableListOf<String>()

    override fun trackEvent(name: String, attributes: Map<String, String>) {
        events += name
    }

    override fun trackMetric(name: String, value: Double, attributes: Map<String, String>) {
        metrics += name to value
    }

    override fun trackError(name: String, throwable: Throwable, attributes: Map<String, String>) {
        errors += name
    }
}
```

Con este fake no estás simulando por comodidad; estás comprobando que la lógica de negocio emite señales cuando corresponde. Ese detalle evita instrumentaciones “decorativas” que solo funcionan en demos.

---

## Qué cambia en tu operación después de este módulo

La diferencia grande es que dejas de reaccionar por intuición y empiezas a reaccionar por evidencia. Si sube la tasa de `sync_failed`, lo ves antes de que soporte te escale diez tickets. Si el tiempo de sync se dispara, lo detectas sin esperar a una avalancha de quejas de lentitud.

En otras palabras, la observabilidad de producción cierra el ciclo completo de ingeniería responsable: construyes, validas en CI, mides en uso real y corriges con foco.

---

## Cierre del módulo

Con este módulo ya no estás “esperando problemas”, estás diseñando cómo enterarte a tiempo y con contexto cuando aparezcan. Esa mentalidad es de equipo que opera producto real, no de equipo que solo entrega código.

En el siguiente tramo del roadmap vamos a usar estas señales para guiar decisiones de arquitectura evolutiva y priorización técnica, conectando lo que medimos con cómo decidimos qué tocar primero en cada iteración.
