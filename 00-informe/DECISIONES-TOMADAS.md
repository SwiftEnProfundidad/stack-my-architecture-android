# Decisiones tomadas

## Registro ADR-EDU-001

- ID: ADR-EDU-001
- Fecha: 2026-02-08
- Decisión: Añadir Nivel Cero explícito antes de Junior.
- Contexto: El público objetivo inicia sin base técnica previa.
- Alternativas evaluadas:
  - Empezar en Junior directamente.
  - Añadir material opcional de repaso sin fase formal.
- Elección: Crear Nivel Cero formal con criterios de paso.
- Impacto: Mejora de progresión pedagógica y reducción de abandono temprano.
- Acciones derivadas:
  - Rediseñar plan curricular en cinco niveles.
  - Añadir evidencias de paso Nivel Cero → Junior.

## Registro ADR-EDU-002

- ID: ADR-EDU-002
- Fecha: 2026-02-08
- Decisión: Fijar matriz técnica estable para evitar bloqueos por versiones.
- Contexto: Cambios de tooling pueden romper prácticas y ejercicios.
- Alternativas evaluadas:
  - Usar siempre “última versión” sin fijar baseline.
  - Fijar baseline y actualizar bajo control.
- Elección: Fijar baseline técnico validado oficialmente y política de actualización.
- Impacto: Mayor estabilidad del entorno de aprendizaje y reproducibilidad.
- Acciones derivadas:
  - Mantener tabla de compatibilidad en informe central.
  - Registrar cualquier cambio técnico como nueva decisión.

## Registro ADR-EDU-003

- ID: ADR-EDU-003
- Fecha: 2026-02-08
- Decisión: Ejecutar implementación por sprint diario con entregables verificables.
- Contexto: El alcance del curso es amplio y requiere control de avance.
- Alternativas evaluadas:
  - Implementación libre sin hitos diarios.
  - Sprint con orden de archivos y criterios de aceptación.
- Elección: Sprint estructurado por días y semanas.
- Impacto: Mejor trazabilidad, control de calidad y menor ambigüedad.
- Acciones derivadas:
  - Mantener `plans/sprint-plan-implementacion.md` como fuente operativa.
  - Validar cada día contra checklist de definición de terminado.

