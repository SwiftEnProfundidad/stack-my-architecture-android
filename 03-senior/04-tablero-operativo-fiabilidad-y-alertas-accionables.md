# Nivel Senior · 04 · Tablero operativo de fiabilidad y alertas que sí ayudan

Cuando un equipo empieza a tomarse en serio la fiabilidad, suele cometer un error muy humano: medir todo. Parece una buena idea porque da sensación de control, pero en la práctica crea un panel enorme, difícil de leer y casi imposible de usar bajo presión. Tener más gráficos no significa tener más claridad.

Un tablero operativo útil no es el que más métricas tiene. Es el que te deja responder rápido tres preguntas muy concretas cuando algo se mueve: qué está fallando, a quién está afectando y qué decisión debemos tomar ahora.

Si el tablero no te da esas respuestas, no es operativo, es decoración.

## El objetivo real de esta lección

Aquí no vamos a construir una “pantalla bonita de observabilidad”. Vamos a construir criterio para seleccionar señales mínimas, definir alertas accionables y evitar fatiga de notificaciones. La meta es que, cuando aparezca una degradación en Android, no pierdas veinte minutos intentando entender qué mirar primero.

Ese tiempo, en incidentes reales, vale muchísimo.

## Qué debería mostrar un tablero que sirve de verdad

Piensa en el tablero como una cabina de vuelo. El piloto no tiene mil indicadores al mismo nivel; tiene un conjunto reducido de señales críticas priorizadas por impacto. En producto Android debería pasar lo mismo.

Para este curso, el tablero de fiabilidad senior se apoya en tres capas de lectura. La primera capa te dice salud global del servicio móvil. La segunda te muestra flujos críticos por versión y por segmento de dispositivo/red. La tercera te ayuda a aislar causas probables cuando algo cae.

No necesitamos complejidad excesiva para empezar. Necesitamos foco.

## Señales mínimas que sí mueven decisiones

Si ya vienes de la lección de SLOs, esto te resultará natural: cada señal del tablero debe estar conectada a un objetivo de servicio o a una hipótesis de impacto. Si no cambia decisiones, sobra.

En una app Android como la del curso, un tablero operativo razonable suele incluir salud de login, latencia de navegación al home, estabilidad de sincronización offline-first y ratio de errores no recuperables por versión activa. Estas señales cubren una parte muy grande del riesgo real para usuario.

La clave no está en nombrarlas bonito. La clave está en que cada una tenga contexto útil para actuar, por ejemplo versión, API level y tipo de red.

## Instrumentación: registrar para decidir, no para coleccionar

Como ya trabajaste contratos desacoplados, podemos mantener la misma disciplina aquí. Creamos un punto de entrada claro para telemetría de fiabilidad y evitamos acoplar dominio a proveedor.

```kotlin
interface OperationalReliabilityTelemetry {
    suspend fun recordSli(
        key: String,
        value: Double,
        appVersion: String,
        androidApiLevel: Int,
        networkType: String
    )

    suspend fun recordFailure(
        key: String,
        reason: String,
        appVersion: String,
        androidApiLevel: Int
    )
}
```

Este contrato parece simple, pero resuelve dos problemas reales. Primero, te obliga a registrar con segmentación mínima desde el origen. Segundo, te permite cambiar backend de observabilidad sin tocar lógica de negocio.

En un caso de uso de sincronización, el registro podría verse así:

```kotlin
class SyncCatalogUseCase(
    private val repository: CatalogRepository,
    private val telemetry: OperationalReliabilityTelemetry,
    private val clock: Clock
) {
    suspend fun execute(): Result<Unit> {
        val start = clock.millis()

        val result = repository.sync()

        val durationMs = (clock.millis() - start).toDouble()

        telemetry.recordSli(
            key = "catalog_sync_duration_ms",
            value = durationMs,
            appVersion = BuildConfig.VERSION_NAME,
            androidApiLevel = Build.VERSION.SDK_INT,
            networkType = "unknown"
        )

        if (result.isFailure) {
            telemetry.recordFailure(
                key = "catalog_sync_failure",
                reason = result.exceptionOrNull()?.message ?: "unknown",
                appVersion = BuildConfig.VERSION_NAME,
                androidApiLevel = Build.VERSION.SDK_INT
            )
        }

        return result
    }
}
```

Observa la intención: primero medimos duración para entender degradación progresiva, luego registramos fallo explícito cuando existe error. Son dos señales distintas y ambas importan. Una te avisa tendencia, la otra te avisa ruptura.

## Alertas accionables: el antídoto contra el ruido

Una alerta mala no solo molesta. También entrena al equipo a ignorar notificaciones. Y cuando llega una alerta crítica, nadie la toma en serio. Esa fatiga es uno de los problemas más caros en operación.

Una alerta accionable tiene que cumplir algo muy concreto: cuando suena, el equipo sabe qué hacer sin inventar protocolo en caliente. Si no está claro qué decisión dispara, no debería existir.

Por eso conviene definir cada alerta junto con su runbook asociado. En vez de “alerta por latencia alta”, define “latencia p95 de login por encima de umbral durante ventana sostenida” y vincúlala con mitigación conocida.

En un documento `docs/reliability/alerts-policy.md` lo puedes dejar así:

```md
# Alerts Policy

Alerta: login_render_p95_regression
Condición: p95 > 2500 ms durante 15 minutos en producción
Severidad: Alta
Acción inmediata:
- Revisar segmentación por app_version
- Si está concentrado en versión reciente, pausar rollout
- Evaluar desactivar flag isNewSessionFlowEnabled
Runbook asociado: docs/runbooks/incident-login-freeze.md
```

Ese enlace entre alerta y acción evita la parálisis típica de “vale, sonó… ¿y ahora qué hacemos?”.

## Diseño del tablero: lectura rápida antes que detalle bonito

Un tablero operativo senior debería abrir con estado resumido de SLOs y budget, luego mostrar flujos críticos y cerrar con señales de diagnóstico. El orden importa porque en incidente primero decides contención, luego investigas profundidad.

Si inviertes este orden, el equipo se pierde en detalle técnico demasiado pronto. Bajo presión, eso cuesta minutos que no tienes.

Por eso, para cada widget del tablero, pregunta siempre: ¿esto ayuda a decidir en los próximos cinco minutos? Si la respuesta es no, probablemente pertenece a un panel de análisis, no a un panel operativo.

## Cadencia de revisión para que el tablero no se oxide

Otro problema común es construir tablero una vez y no tocarlo nunca. El producto cambia, los riesgos cambian y las señales útiles también. Si no revisas, terminas operando con un mapa viejo.

Una revisión corta, recurrente y pragmática suele ser suficiente. Revisas si las alertas fueron útiles, si hubo ruido innecesario, si faltó visibilidad en incidentes recientes y qué señal nueva merece entrar. Lo importante no es la ceremonia, es la mejora continua del sistema.

## Ejemplo de decisión con tablero en tiempo real

Supongamos que durante una tarde ves que crash-free rate se mantiene alta, pero el panel de flujo crítico muestra caída de `login_success_to_home_render` y aumento de `catalog_sync_duration_ms` en Android 14 con red móvil. Sin tablero orientado a decisión, puedes pensar que “no hay crisis porque no hay crash”.

Con tablero bien diseñado entiendes rápido que tienes degradación funcional seria sin caída catastrófica. Eso cambia el tipo de respuesta: no necesitas rollback inmediato de toda la versión, pero sí pausar expansión y aplicar mitigación focalizada en el flujo afectado.

Ese matiz evita tanto sub-reacción como sobre-reacción.

## Cierre de la lección

Un tablero operativo no existe para impresionar en demos. Existe para ayudarte a proteger usuarios y tomar decisiones bajo incertidumbre con menos fricción.

Si lo construyes con señales conectadas a objetivos, alertas con acción clara y revisión viva, se convierte en una pieza central de madurez senior en Android.

En la siguiente lección vamos a cerrar este tramo conectando todo lo que llevas hasta ahora en un modelo de gobernanza técnica de sprint: cómo negociar capacidad entre fiabilidad y roadmap sin volver al caos de prioridades cambiantes.