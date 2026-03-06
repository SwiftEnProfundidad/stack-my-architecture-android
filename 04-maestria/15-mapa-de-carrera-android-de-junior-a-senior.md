# Nivel Maestría · 15 · Mapa de carrera Android: de junior a senior con criterio

Cuando alguien empieza en Android suele pensar que crecer profesionalmente significa aprender más librerías o dominar más APIs. Con el tiempo descubres que eso ayuda, pero no es lo que realmente te hace avanzar de nivel. Lo que te hace avanzar es cómo decides, cómo colaboras y cómo respondes cuando el sistema se vuelve incierto.

Esta lección existe para cerrar el curso con una brújula de carrera realista. No para que te compares con nadie, sino para que tengas claridad sobre qué señales indican que estás evolucionando bien.

En una etapa inicial, el foco principal está en ejecutar tareas con calidad y pedir contexto cuando algo no encaja. Aquí se construyen hábitos muy importantes: escribir código legible, testear lo esencial, no esconder errores y entender impacto de los cambios antes de abrir un PR. Puede parecer básico, pero es justo lo que sostiene todo lo demás.

Cuando pasas a una etapa intermedia, el salto no es solo técnico, es sistémico. Empiezas a pensar en dependencias entre piezas, en contratos entre features y en cómo evitar que una decisión local rompa el producto global. Este punto marca la diferencia entre “resuelvo tickets” y “construyo producto de forma sostenible”.

En etapa senior, la responsabilidad cambia otra vez. Ya no se trata solo de escribir buen código tú; se trata de crear condiciones para que el equipo completo entregue bien bajo presión. Eso incluye gobernanza de calidad, manejo de incidentes, decisiones de release y priorización entre roadmap y fiabilidad sin caer en extremos.

```kotlin
package com.stackmyarchitecture.career

data class CareerSignal(
    val technicalDepth: Int,
    val systemThinking: Int,
    val deliveryReliability: Int,
    val mentoringImpact: Int
)

class CareerProgressEvaluator {
    fun summarize(signal: CareerSignal): String {
        val global = (signal.technicalDepth + signal.systemThinking + signal.deliveryReliability + signal.mentoringImpact) / 4
        return "Progreso global estimado: $global/10"
    }
}
```

Este ejemplo no pretende etiquetarte con un número. Sirve para recordar que la carrera técnica no es un eje único. Puedes tener mucha profundidad técnica y aún necesitar crecer en comunicación o en impacto de equipo. Mirar la evolución con varias dimensiones te evita caer en diagnósticos simplistas.

También es importante cuidar algo que casi nadie te dice al principio: tu reputación técnica se construye en los momentos incómodos. Cuando hay un bug difícil, cuando hay desacuerdo de arquitectura, cuando hay presión de release. En esos escenarios, la gente observa no solo si aciertas, sino cómo piensas y cómo colaboras.

Si mantienes una práctica constante de decisiones explícitas, aprendizaje observable y comunicación clara, el crecimiento se vuelve acumulativo. No depende de “tener suerte” con un proyecto brillante. Depende de mostrar criterio de forma sostenida.

Con esta lección cerramos de forma completa la ruta de Maestría. A partir de aquí, tu evolución profesional ya no necesita una guía lineal. Necesita práctica consciente, feedback honesto y decisiones cada vez más claras en sistemas reales.

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

---

## Ejercicio guiado

**Objetivo**: Autoevaluar en escala 1-5 cada competencia del mapa de carrera Android.

**Pasos**:
1. Puntúa cada competencia en una escala honesta de 1 a 5: 1 = no lo conozco, 2 = lo entiendo pero no lo aplico, 3 = lo aplico con ayuda, 4 = lo aplico de forma autónoma, 5 = lo enseño y lo defiendo bajo presión.
2. Rellena la tabla para las cuatro dimensiones del modelo `CareerSignal`: profundidad técnica, pensamiento sistémico, fiabilidad de entrega y mentoría/impacto en el equipo.
3. Para las competencias con puntuación 1 o 2, escribe una acción concreta que puedas hacer esta semana para subirla un punto.
4. Calcula tu media por dimensión y por global.
5. Condición de éxito: tienes la tabla completa con puntuaciones honestas, al menos una acción concreta por cada dimensión con puntuación ≤ 2, y un número global que puedes revisar en 90 días para medir progreso real.

<details>
<summary>Solución de referencia</summary>

| Dimensión | Competencia específica | Puntuación (1-5) | Acción si ≤ 2 |
|---|---|---|---|
| Profundidad técnica | Arquitectura multi-módulo con contratos | 3 | — |
| Profundidad técnica | Testing: unitario + integración + UI | 2 | Esta semana: escribir 3 tests de integración para el DAO principal |
| Profundidad técnica | Rendimiento: benchmark + baseline profile | 2 | Esta semana: ejecutar benchmark existente y leer el resultado |
| Pensamiento sistémico | Bounded contexts y ownership | 3 | — |
| Pensamiento sistémico | Migraciones sin bloqueo | 2 | Esta semana: diseñar la migración Room del ejercicio de lección 04 |
| Fiabilidad de entrega | SLOs y error budgets | 2 | Esta semana: definir 1 SLO para el flujo de sincronización |
| Fiabilidad de entrega | Releases graduales y rollback | 3 | — |
| Mentoría / impacto | Revisión de PRs con criterio explicado | 4 | — |
| Mentoría / impacto | Defensa técnica con datos ante no técnicos | 2 | Esta semana: escribir 1 párrafo explicando una decisión de arquitectura sin usar jerga |

**Media por dimensión**: Técnica: 2.3 · Sistémica: 2.5 · Fiabilidad: 2.5 · Mentoría: 3.0 · **Global: 2.6/5**

**Resultado esperado**: El alumno tiene un mapa de carrera personalizado con evidencia honesta de su estado actual y acciones concretas para la semana siguiente, no una valoración abstracta.

</details>

La lectura del diagrama sigue esta semántica:
1. `-->` dependencia directa en runtime.
2. `-.->` wiring o configuración.
3. `==>` contrato o abstracción.
4. `--o` salida o propagación de resultado.
