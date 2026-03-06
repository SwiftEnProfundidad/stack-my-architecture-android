# Nivel Senior · 06 · Simulación completa de sprint bajo presión: cómo decidir sin improvisar

Ya tienes las piezas técnicas del bloque Senior: sabes medir salud operativa, conoces error budgets, tienes runbooks y levantaste una policy de gobernanza para orientar capacidad. El reto real ahora no es aprender otra pieza aislada. El reto es usarlas juntas cuando todo llega a la vez: presión de negocio, señales de degradación y miedo a que una mala apuesta dispare incidentes.

Esta lección es una simulación integral para entrenar ese momento.

## Escenario realista de entrada al planning

Es lunes por la mañana y el equipo Android abre planning con tres tensiones activas. Producto quiere liberar una mejora de onboarding comprometida con marketing. Soporte reporta aumento de quejas de lentitud en login para parte de usuarios Android 14. El panel operativo muestra degradación intermitente en `login_success_to_home_render` y el budget de login está en 19%.

No estás en modo crisis total, pero tampoco estás en un estado sano. Ese matiz importa porque es justo el tipo de contexto donde un equipo sin marco suele cometer errores caros: o bloquea todo por miedo, o ignora señales por urgencia comercial.

## Qué ocurre si el equipo decide por intuición

Si no existe método, la reunión se vuelve una puja de prioridades. Quien trae presión más visible inclina la balanza. El resultado puede ser un sprint aparentemente ambicioso que añade riesgo al flujo más frágil, o un sprint excesivamente conservador que frena valor de negocio sin un criterio proporcional al riesgo real.

Ambas salidas son ineficientes porque no transforman datos en decisión. Solo transforman tensión en reacción.

## Aplicar el marco de gobernanza del módulo anterior

La simulación arranca con una regla básica: antes de discutir historias, se fija el modo de capacidad del sprint con estado operativo actual. Con budget crítico en 19% y degradación activa en flujo core, la recomendación cae en `RELIABILITY_HEAVY`.

Aquí aparece una decisión adulta que suele faltar en equipos jóvenes: separar objetivo de negocio en entregables de riesgo distinto. La mejora de onboarding no se cancela completa; se divide. La parte que no toca login crítico puede avanzar. La parte que altera el camino sensible se condiciona a recuperación de margen operativo.

Eso protege dos cosas al mismo tiempo: la confianza del usuario y la credibilidad del roadmap.

## Traducir la decisión a un plan de sprint ejecutable

Con ese modo de capacidad, el sprint queda diseñado en torno a tres líneas que se apoyan mutuamente. La primera es estabilización del flujo degradado, con acciones técnicas medibles en p95 y tasa de éxito de login. La segunda es avance de producto en cambios de riesgo medio o bajo fuera del cuello de botella actual. La tercera es refuerzo de observabilidad para detectar recaídas temprano durante rollout posterior.

La clave aquí no es repartir tareas por porcentaje rígido. La clave es que cada bloque tenga una hipótesis clara de impacto y una señal de verificación.

## Dejar trazabilidad explícita de la decisión

Para que esta gobernanza sobreviva a cambios de personas y memoria de sprint, conviene registrar decisión y condición de salida en un artefacto versionado.

```md
# Sprint 12 Decision Record

Contexto operativo
- Budget de login: 19%
- Degradación activa en login_success_to_home_render (p95)
- Incidente severo reciente en últimos 14 días

Decisión de capacidad
- Modo: RELIABILITY_HEAVY

Alcance del sprint
- Recuperación de login: optimización de render + endurecimiento de fallback de sesión
- Roadmap: onboarding parcial sin cambios en camino crítico de login

Condición para reabrir cambios de alto riesgo en login
- Budget de login > 35%
- 7 días sin alerta crítica sostenida en login
```

Este registro resuelve un problema muy común: dos sprints después nadie recuerda por qué se partió una entrega. Con decisión record, el equipo puede auditar coherencia entre lo que prometió y lo que realmente observó.

## Mitad de sprint: revalidar o corregir rumbo

El error más caro en este tipo de planificación es decidir el lunes y no volver a mirar señales hasta la retrospectiva. Por eso la simulación incluye una revisión de mitad de sprint donde se compara tendencia real frente a hipótesis inicial.

Puedes modelar esta revisión con un caso de uso pequeño que avise si hay que escalar recuperación.

```kotlin
class MidSprintReliabilityCheckUseCase(
    private val governanceRepository: ReliabilityGovernanceRepository
) {
    suspend fun shouldEscalateRecovery(): Boolean {
        val snapshot = governanceRepository.getSnapshot()

        val criticalBudget = minOf(
            snapshot.loginBudgetRemaining,
            snapshot.syncBudgetRemaining
        )

        return snapshot.isCriticalDegradationActive || criticalBudget < 0.15
    }
}
```

La decisión de usar `minOf` mantiene foco en el punto más débil del sistema. El umbral `< 0.15` no es mágico ni universal; es un guardrail inicial para evitar seguir asumiendo riesgo cuando el margen ya es muy estrecho. Lo correcto es calibrarlo con histórico del producto.

## Qué hacer si la tendencia no mejora

Si la revisión de mitad de sprint muestra que login sigue degradado o el budget sigue cayendo, el equipo no espera al cierre para reaccionar. Reduce riesgo adicional, prioriza mitigación más agresiva y renegocia alcance de roadmap con base en la condición acordada al inicio.

Esta parte es crítica porque convierte la gobernanza en sistema vivo y no en ritual inicial.

## Qué hace que esta simulación sea realmente senior

La diferencia no está en usar palabras como SLO o budget. La diferencia está en el comportamiento del equipo bajo tensión: decidir con contexto compartido, registrar supuestos, revisar señales en tiempo y corregir sin drama político.

Cuando eso ocurre, fiabilidad y roadmap dejan de vivirse como guerra de áreas. Se convierten en una negociación técnica-profesional sostenida por evidencia.

## Cierre de la lección

Esta simulación deja un aprendizaje operativo muy concreto. En Android real no gana el equipo que "siempre entrega rápido" ni el que "siempre juega seguro". Gana el que sabe mover el peso entre entrega y estabilidad según salud del sistema, con reglas claras y capacidad de ajuste.

Ese criterio es el puente natural hacia Maestría, donde ahora vas a escalar estas mismas decisiones al nivel de varios dominios y varios equipos coordinándose sin perder autonomía.

---

## Ejercicio guiado

**Objetivo**: Simular la decisión de rollback versus hotfix ante un incidente de login degradado en producción, aplicando el marco de gobernanza del sprint.

**Pasos**:
1. Dado el escenario: budget de login al 19%, `p95_login_render > 3500 ms` durante 20 minutos, último release hace 4 horas con flag `isNewSessionFlowEnabled` activo. Evalúa con `SprintCapacityEvaluator` (o lógica equivalente) si el modo debe cambiar a `RELIABILITY_HEAVY`.
2. Describe en texto la decisión principal: ¿desactivas el flag primero (mitigación), haces rollback de versión (reversión) o aplicas hotfix (corrección urgente)? Justifica el orden.
3. Escribe en Kotlin un `MidSprintCheck` que devuelva `shouldRollback = true` si el budget de login es < 15% Y la degradación lleva más de 15 minutos activa.
4. Condición de éxito: el código compila, el test con `loginBudget = 0.14` y `degradationMinutes = 20` devuelve `shouldRollback = true`, y la justificación escrita sigue el orden: mitigar → observar → rollback si no mejora.

<details>
<summary>Solución de referencia</summary>

```kotlin
// 3. Lógica de decisión de rollback
data class MidSprintIncidentContext(
    val loginBudgetRemaining: Double,    // fracción restante, p. ej. 0.14
    val degradationActiveMinutes: Int
)

data class RollbackDecision(
    val shouldRollback: Boolean,
    val reason: String
)

class MidSprintCheck {
    fun evaluate(context: MidSprintIncidentContext): RollbackDecision {
        val budgetCritical      = context.loginBudgetRemaining < 0.15
        val degradationSustained = context.degradationActiveMinutes >= 15

        return if (budgetCritical && degradationSustained) {
            RollbackDecision(
                shouldRollback = true,
                reason = "Budget crítico (${(context.loginBudgetRemaining * 100).toInt()}%) " +
                         "y degradación sostenida ${context.degradationActiveMinutes} min → rollback recomendado"
            )
        } else {
            RollbackDecision(
                shouldRollback = false,
                reason = "Situación bajo umbral; mantener mitigación activa y monitorear"
            )
        }
    }
}

// Test de verificación
fun main() {
    val checker = MidSprintCheck()

    val scenarioA = MidSprintIncidentContext(
        loginBudgetRemaining   = 0.14,
        degradationActiveMinutes = 20
    )
    val decisionA = checker.evaluate(scenarioA)
    println("Escenario A - shouldRollback: ${decisionA.shouldRollback}")  // true
    println("Razón: ${decisionA.reason}")

    val scenarioB = MidSprintIncidentContext(
        loginBudgetRemaining   = 0.20,
        degradationActiveMinutes = 10
    )
    val decisionB = checker.evaluate(scenarioB)
    println("Escenario B - shouldRollback: ${decisionB.shouldRollback}")  // false
}

/*
 * 2. Justificación del orden de decisión:
 *
 * Paso 1 · Mitigar: desactivar flag isNewSessionFlowEnabled → observar recuperación 15 min.
 * Paso 2 · Observar: si p95 baja a < 2500 ms y budget se estabiliza → continuar sin rollback.
 * Paso 3 · Rollback: si budget < 15% Y degradación sigue activa > 15 min → revertir versión.
 *
 * Este orden minimiza el impacto operativo: el flag es la palanca más rápida y reversible;
 * el rollback completo es la última opción porque afecta también a usuarios sin problemas.
 */
```

**Resultado esperado**: `MidSprintCheck.evaluate` devuelve `shouldRollback = true` con `loginBudget = 0.14` y `degradationMinutes = 20`, y `false` con `loginBudget = 0.20` y `degradationMinutes = 10`; la decisión documentada sigue el orden mitigar → observar → rollback con justificación basada en datos.

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
