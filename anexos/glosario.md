# Glosario Android

Términos clave del curso Android, ordenados para que el alumno pueda volver a la primera lección donde aparece cada concepto importante.

---

| Término | Definición | Primera aparición |
|---------|-----------|-------------------|
| **AGP** | Android Gradle Plugin. Conecta Gradle con el toolchain Android y define buena parte del proceso de build. | `01-junior/00-setup-junior.md` |
| **Baseline Profile** | Perfil de rendimiento que ayuda a acelerar arranque y rutas críticas en producción. | `02-midlevel/07-performance-ci-macrobenchmark-baselineprofiles.md` |
| **Bounded Context** | Límite semántico y organizativo donde un modelo tiene significado preciso y ownership claro. | `04-maestria/02-bounded-contexts-y-ownership-tecnico.md` |
| **CI** | Integración continua. Pipeline automático que valida calidad antes de mergear o publicar. | `02-midlevel/06-quality-gates-ci-offline-sync.md` |
| **Compose** | Toolkit declarativo moderno para construir UI en Android. | `00-nivel-cero/09-primera-app-compose.md` |
| **Composable** | Función anotada con `@Composable` que describe una parte de la interfaz. | `00-nivel-cero/09-primera-app-compose.md` |
| **Composition Root** | Punto donde se ensamblan dependencias y wiring de una feature o de toda la app. | `00-core-mobile/10-plantillas.md` |
| **Contrato** | Acuerdo explícito entre módulos, features o capas sobre qué se expone y cómo evoluciona. | `00-core-mobile/07-apis-contratos-versionado.md` |
| **Coroutines** | Modelo de concurrencia de Kotlin para trabajo asíncrono estructurado. | `01-junior/00-setup-junior.md` |
| **DAO** | Data Access Object. Interfaz que encapsula acceso a base de datos en Room. | `01-junior/05-room-offline-first.md` |
| **DataStore** | Persistencia ligera para preferencias o estado simple, no para datos complejos de negocio. | `01-junior/06-datastore-estado-ligero.md` |
| **Deep Link** | Ruta externa que abre una pantalla concreta de la app. | `02-midlevel/12-evolucion-navegacion-y-deeplinks-compatibles.md` |
| **Dependency governance** | Reglas de entrada, aprobación y mantenimiento de dependencias para evitar caos estructural. | `00-core-mobile/09-dependency-governance-supply-chain.md` |
| **DTO** | Objeto de transporte de datos, separado del modelo de dominio. | `02-midlevel/01-red-robusta-retrofit-okhttp.md` |
| **Entidad** | Modelo con identidad propia que persiste en el tiempo. | `00-core-mobile/02-invariantes-y-contratos.md` |
| **Error budget** | Presupuesto de fallos aceptable antes de priorizar estabilidad sobre nuevas features. | `03-senior/03-slos-error-budgets-priorizacion-fiabilidad.md` |
| **Feature flag** | Interruptor configurable para activar o desactivar comportamiento sin redeploy completo. | `00-core-mobile/06-release-rollback-flags.md` |
| **Feature-First** | Organización vertical del código por capacidades completas del producto. | `01-junior/01-arquitectura-android-recomendada.md` |
| **Flow** | Stream asíncrono de Kotlin para emitir valores en el tiempo. | `01-junior/01-arquitectura-android-recomendada.md` |
| **Gradle** | Sistema de build que compila, empaqueta y automatiza tareas del proyecto. | `01-junior/00-setup-junior.md` |
| **Hilt** | Solución de inyección de dependencias para Android basada en Dagger. | `01-junior/04-hilt-integracion-inicial.md` |
| **Invariante** | Regla que siempre debe cumplirse dentro del dominio o del contrato de una capa. | `00-core-mobile/02-invariantes-y-contratos.md` |
| **JDK** | Java Development Kit usado por Gradle y Android Studio para compilar. | `01-junior/00-setup-junior.md` |
| **Kotlin** | Lenguaje principal del stack Android moderno del curso. | `00-nivel-cero/03-primer-kotlin.md` |
| **Macrobenchmark** | Medición automatizada de rendimiento a nivel de app o de flujos críticos. | `02-midlevel/07-performance-ci-macrobenchmark-baselineprofiles.md` |
| **Métrica accionable** | Señal que sirve para decidir, no solo para decorar dashboards. | `02-midlevel/08-observabilidad-produccion-metricas-alertas.md` |
| **Modulo compartido** | Módulo intermedio usado para exponer contratos o kernel común sin acoplar features entre sí. | `02-midlevel/10-gobernanza-dependencias-entre-features.md` |
| **Navigation Compose** | Librería de navegación moderna para Compose. | `01-junior/03-navegacion-moderna-navigation-compose.md` |
| **Offline-first** | Enfoque en el que la app sigue siendo útil con mala red o sin red. | `01-junior/05-room-offline-first.md` |
| **Observabilidad** | Conjunto de logs, métricas y trazas útiles para entender qué está pasando en runtime. | `02-midlevel/04-observabilidad-y-diagnostico.md` |
| **Ownership** | Responsabilidad técnica clara sobre un bounded context, módulo o contrato. | `04-maestria/02-bounded-contexts-y-ownership-tecnico.md` |
| **Quality gate** | Validación automática que bloquea promoción de cambios inseguros. | `02-midlevel/06-quality-gates-ci-offline-sync.md` |
| **Repositorio** | Capa que coordina fuentes de datos y expone operaciones con semántica de dominio. | `01-junior/02-feature-base-practica.md` |
| **Retrofit** | Cliente HTTP tipado habitual en Android para consumir APIs. | `02-midlevel/01-red-robusta-retrofit-okhttp.md` |
| **Rollback** | Estrategia para volver atrás o mitigar rápido un cambio peligroso. | `03-senior/01-release-strategy-y-rollback-seguro.md` |
| **Room** | Capa de persistencia estructurada sobre SQLite para Android. | `01-junior/05-room-offline-first.md` |
| **Runbook** | Procedimiento operativo para responder a incidencias o degradaciones. | `03-senior/02-incident-response-y-runbooks-operativos.md` |
| **SLO** | Objetivo medible de fiabilidad o rendimiento. | `03-senior/03-slos-error-budgets-priorizacion-fiabilidad.md` |
| **Sync state** | Estado que indica si un dato está pendiente, sincronizado o en error respecto al backend. | `02-midlevel/02-offline-first-sincronizacion.md` |
| **Task / coroutine estructurada** | Trabajo asíncrono que vive dentro de una jerarquía controlada y cancelable. | `01-junior/00-setup-junior.md` |
| **Test de integración** | Test que valida colaboración real entre varios componentes. | `02-midlevel/05-pruebas-de-integracion-offline-sync.md` |
| **UDF** | Unidirectional Data Flow: eventos suben, estado baja. | `01-junior/01-arquitectura-android-recomendada.md` |
| **Use case** | Operación de aplicación que coordina reglas y dependencias para cumplir una intención concreta. | `00-core-mobile/10-plantillas.md` |
| **ViewModel** | Clase que gestiona estado de pantalla y lógica de presentación desacoplada de la UI. | `01-junior/01-arquitectura-android-recomendada.md` |
| **WorkManager** | Framework para trabajo diferido y persistente que debe sobrevivir a cierres o reinicios. | `01-junior/07-workmanager-tareas-persistentes.md` |

---

## Cómo usar este glosario

1. Si un término aparece y no lo dominas, vuelve a su **primera aparición**.
2. Si dos conceptos se parecen, compáralos con ejemplos del scaffold real del curso.
3. Si una lección introduce un término nuevo importante, añádelo aquí al cerrar esa etapa.
