# Brief del proyecto final

Este archivo existe para mantener compatibilidad con el plan de implementación y con las referencias pedagógicas que usan el nombre `00-brief.md`.

El contenido oficial del proyecto final está en [`00-brief-ruralgo-fieldops.md`](00-brief-ruralgo-fieldops.md). Ese documento define el alcance funcional, técnico y operativo de RuralGO FieldOps como producto vivo transversal del curso.

## Qué valida esta etapa de forma explícita

Esta etapa no valida solo desarrollo de features. Valida capacidad de entrega profesional extremo a extremo:

1. Diseño técnico con límites claros y trade-offs explícitos.
2. Implementación con calidad y cobertura suficiente en caminos críticos.
3. Operación realista (observabilidad, incident response y release controlado).
4. Defensa técnica basada en evidencia, no en opinión.

## Criterio de cierre enterprise

Para considerar el proyecto final cerrado se exige:

1. Alcance funcional obligatorio implementado.
2. Rúbrica final aprobada sin bloqueadores críticos.
3. Evidencias obligatorias completas y verificables por tercero.
4. Narrativa de defensa técnica coherente con lo implementado.

## Referencias obligatorias de esta etapa

1. Brief integral del reto:
- [`00-brief-ruralgo-fieldops.md`](00-brief-ruralgo-fieldops.md)

2. Rúbrica de empleabilidad:
- [`01-rubrica-empleabilidad.md`](01-rubrica-empleabilidad.md)

3. Evidencias obligatorias:
- [`02-evidencias-obligatorias.md`](02-evidencias-obligatorias.md)

4. Operación y gobernanza:
- [`03-operacion-senior.md`](03-operacion-senior.md)
- [`04-gobernanza-maestria.md`](04-gobernanza-maestria.md)

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
  UC -.o PORT
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

La lectura del diagrama sigue esta semantica:
1. `-->` dependencia directa en runtime.
2. `-.->` wiring o configuracion.
3. `-.o` dependencia contra contrato/abstraccion.
4. `--o` salida o propagacion de resultado.
