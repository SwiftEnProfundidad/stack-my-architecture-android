# Rubrica de gates por fase - Android

## Objetivo
Definir criterios de aprobado/rechazado por fase para asegurar progresion real.

## Gates por fase

| Fase | Gate tecnico | Gate pedagogico | Gate de defensa |
| --- | --- | --- | --- |
| Core Mobile + Nivel Cero | Diagrama de capas y limites correcto | Explica semantica de flechas | Defiende una dependencia valida y una invalida |
| Junior | Flujo rojo-verde-refactor completo | Explica como aisla feature de framework | Defiende por que elegiste ese boundary |
| Midlevel | Offline-first y sync en verde | Explica conflicto y resolucion | Defiende trade-off consistencia vs latencia |
| Senior | Observabilidad y quality gates activos | Explica impacto de metricas | Defiende decision de hardening por riesgo |
| Maestria | Release readiness y runbook validado | Explica criterio de readiness | Defiende plan de rollback y mitigacion |
| Proyecto Final | Integracion end-to-end reproducible | Explica arquitectura completa | Defiende roadmap de evolucion |

## Regla de aprobado
1. Se aprueba fase solo con los tres gates en verde.
2. Si un gate falla, se registra recuperacion con evidencia faltante.
3. Todo gate debe trazarse a comando, test o artefacto versionado.

## Evidencia de recuperacion
1. Causa del fallo.
2. Cambio aplicado.
3. Prueba de cierre.
4. Leccion aprendida.
