# Scorecard de empleabilidad - Android

## Objetivo
Mapear niveles del curso a senales observables de contratacion y defensa tecnica.

## Seniority map

| Nivel | Senal en entrevista | Evidencia portfolio | Riesgo si falta |
| --- | --- | --- | --- |
| Junior | Explica clean architecture y testing base | Feature Android completa con tests | Implementacion acoplada y fragil |
| Mid | Defiende offline-first y contratos internos | Integracion Room/Worker/API con pruebas | Arquitectura no escalable |
| Senior | Decide con metricas y calidad operativa | Dashboard de metricas + quality gates | Decisiones sin observabilidad |
| Arquitecto | Coordina modulos y limites de ownership | ADR + diagrama inter-modulo + governance | Sistema dificil de evolucionar |
| Maestria | Opera release con control de riesgo | Runbook + estrategia rollout/rollback | Riesgo alto en produccion |

## Criterio de empleabilidad
1. Cada nivel requiere evidencia ejecutable.
2. Cada evidencia incluye defensa de decision.
3. La defensa cubre riesgo, mitigacion y alternativa descartada.

## Checklist de defensa tecnica
- Problema y contexto
- Invariantes
- Opciones evaluadas
- Decision final
- Riesgo y mitigacion
- Validacion en runtime
