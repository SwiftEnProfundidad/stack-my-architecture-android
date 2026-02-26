# Guía rápida: leyenda de flechas Mermaid

Referencia base para mantener semántica de dependencias consistente en diagramas del curso.

```mermaid
flowchart LR
    UI[Compose UI] --> VM[ViewModel]
    VM -.-> DI[Hilt Module]
    VM -.o PORT[Repository Interface]
    VM --o OUT[Telemetry / Event Output]
```

## Convención

- `-->` Dependencia directa (runtime).
- `-.->` Wiring / configuración.
- `-.o` Contrato / abstracción.
- `--o` Salida / propagación.
