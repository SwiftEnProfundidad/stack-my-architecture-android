# Entregables de Nivel Cero

Has llegado al cierre de Nivel Cero. Este documento existe para que compruebes si realmente estás preparado para pasar al siguiente nivel. Aquí no medimos memorización. Medimos comprensión aplicada.

El primer entregable obligatorio es tu proyecto “Rutina Diaria” funcionando con flujo completo. Eso significa que debe existir una pantalla de inicio, una pantalla de entrada de rutina y una pantalla de resumen. También significa que la validación del input debe responder correctamente cuando el texto está vacío y cuando el texto es válido.

El segundo entregable obligatorio es la evidencia visual de ejecución. Debes guardar capturas de cada pantalla en funcionamiento y, si puedes, un pequeño vídeo de menos de un minuto mostrando el flujo completo desde inicio hasta resumen.

El tercer entregable obligatorio es la evidencia de comprensión escrita. Debes redactar una explicación corta donde cuentes qué aprendiste sobre variables, condicionales, funciones y navegación, y cómo se conectan entre sí dentro de tu app.

El cuarto entregable obligatorio es la autoevaluación de errores. Debes identificar al menos tres errores que hayas cometido durante Nivel Cero, explicar por qué ocurrieron y describir cómo los corregiste. Esta parte es muy importante porque demuestra que sabes aprender de tus fallos.

Para considerar Nivel Cero como completado, el equipo docente debe poder verificar que tu app funciona, que tu lógica es coherente y que tu explicación demuestra comprensión real. Si falta alguna de estas piezas, no pasa nada, simplemente se corrige y se vuelve a intentar con guía.

Cuando cumplas estos entregables, tendrás una base sólida para entrar a Junior con confianza y sin saltos bruscos de dificultad.


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

La lectura del diagrama sigue esta semantica:
1. `-->` dependencia directa en runtime.
2. `-.->` wiring o configuracion.
3. `==>` contrato o abstraccion.
4. `--o` salida o propagacion de resultado.
