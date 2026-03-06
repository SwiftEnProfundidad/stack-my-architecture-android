# Checkpoint y bitácora - Etapa 1: Junior

Este cierre valida que ya sabes construir una feature Android profesional inicial con Compose, ViewModel, repositorio, DI y persistencia básica. Junior no se supera por acumular APIs: se supera cuando tus decisiones empiezan a tener estructura.

## Qué debes poder hacer antes de avanzar

- Levantar una feature completa con flujo de eventos, estado y renderizado UI.
- Usar `Navigation Compose` sin acoplar pantallas entre sí de forma caótica.
- Inyectar dependencias con Hilt sin convertirlo en “magia negra”.
- Distinguir cuándo usar `Room`, cuándo `DataStore` y cuándo `WorkManager`.
- Tener pruebas mínimas de UI y de ViewModel que realmente validen comportamiento.

## Checklist de cierre

- [ ] Puedo explicar el flujo `evento -> ViewModel -> repositorio -> fuente de datos -> estado UI`.
- [ ] Tengo una feature que no mezcla queries, renderizado y persistencia en el composable.
- [ ] Sé justificar por qué un dato vive en `Room` o en `DataStore`.
- [ ] Tengo al menos una tarea persistente con `WorkManager` y sé por qué necesita constraints.
- [ ] He ejecutado pruebas UI y unitarias que fallan si rompo un flujo real.

## Mini-quiz de autoevaluación

1. ¿Qué responsabilidad no debería asumir nunca un composable?
2. ¿Por qué un `ViewModel` no debería conocer detalles de Room o Retrofit directamente?
3. ¿Qué diferencia funcional hay entre `Room` y `DataStore`?
4. ¿Cuándo tiene sentido usar `WorkManager` frente a una coroutine normal?
5. ¿Qué te demuestra una prueba UI que no te demuestra una demo manual?

## Evidencias mínimas

- Feature navegable con arquitectura coherente.
- Persistencia local mínima combinando `Room` y `DataStore` cuando aplique.
- Pruebas de UI y unitarias ejecutables.
- Diagrama básico del flujo de la feature.

## Bitácora guiada

### Lo que ya domino

Resume qué piezas de la arquitectura Android ya puedes montar desde cero.

### Lo que aún me cuesta

Indica si tu principal dificultad está en DI, navegación, persistencia o testing.

### Decisión técnica mejor entendida

Explica una decisión de tu feature que ahora sabes defender con criterio.

### Error estructural detectado

Anota un acoplamiento o mezcla de responsabilidades que encontraste y cómo lo corregiste.

### Próximo paso

Describe qué necesitas reforzar para entrar en Midlevel sin convertir offline-first en un parche improvisado.
