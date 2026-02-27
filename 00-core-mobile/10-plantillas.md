# Plantillas operativas (copy/paste)

## ADR template

Contexto:

Decisión:

Trade-offs:

Consecuencias:

Métricas:

## RFC template

Problema:

Opciones:

Recomendación:

Rollout:

## PR Review checklist

- [ ] Arquitectura: límites y dependencias correctos.
- [ ] Tests: cobertura suficiente del impacto.
- [ ] Edge cases: fallos previsibles cubiertos.
- [ ] Observabilidad: logs/métricas para diagnóstico.
- [ ] Seguridad/privacidad: PII/secretos revisados.

## DoD template

Build:

Tests:

Quality gates:

## Metrics before/after table template

| Métrica | Before | After | Delta | Evidencia |
|---|---:|---:|---:|---|
| | | | | |
| | | | | |


<!-- auto-gapfix:layered-mermaid -->
## Diagrama de arquitectura por capas

```mermaid
flowchart LR
  subgraph CORE[Core / Domain]
    C1[Entity]
    C2[Rule]
  end

  subgraph APP[Application]
    A1[UseCase]
    A2[Port]
  end

  subgraph UI[Interface]
    U1[ViewModel]
    U2[Screen]
  end

  subgraph INFRA[Infrastructure]
    I1[RemoteDataSource]
    I2[LocalDataSource]
  end

  A1 --> C1
  A1 -.-> A2
  U1 -.o A1
  A1 --o U1
  A2 -.-> I1
  A2 -.-> I2
```

La lectura del diagrama sigue esta semantica:
1. `-->` dependencia directa en runtime.
2. `-.->` contrato o abstraccion.
3. `-.o` wiring o composicion.
4. `--o` salida o propagacion de resultado.

<!-- auto-gapfix:layered-snippet -->
## Snippet de referencia por capas

```kotlin
interface FeaturePort {
    suspend fun fetch(): List<String>
}

class FeatureUseCase(
    private val port: FeaturePort
) {
    suspend operator fun invoke(): List<String> = port.fetch()
}

class FeatureViewModel(
    private val useCase: FeatureUseCase
) : ViewModel() {

    private val _items = MutableStateFlow<List<String>>(emptyList())
    val items: StateFlow<List<String>> = _items

    fun load() {
        viewModelScope.launch {
            _items.value = runCatching { useCase() }.getOrDefault(emptyList())
        }
    }
}
```
