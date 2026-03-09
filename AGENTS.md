# AGENTS.md - stack-my-architecture-android

## Idioma y comunicación
- MUST: Responder siempre en español.
- MUST: Mantener trazabilidad en cada entrega (`escenario -> tests -> evidencia -> task`).
- MUST: Al cerrar cada iteración, responder siempre con `MD de seguimiento` y `task actual`.

## Project mode
- PROJECT MODE: brownfield

## Método
- REQUIRED SKILL: `enterprise-operating-system`

## Fuente de verdad
- MUST: La autoridad documental local vive en [README.md](/Users/juancarlosmerlosalbarracin/Developer/Projects/stack-my-architecture/stack-my-architecture-android/README.md), `docs/` y `anexos/`.
- MUST: La cadena de skills del repo se resuelve por `AGENTS.md -> vendor/skills -> skills.sources.json -> skills.lock.json`.

## Skills requeridos
- REQUIRED SKILL: `android-enterprise-rules`

## Reglas del modo
- MUST: No tocar `proyecto-android/` ni material didáctico salvo petición explícita.
- MUST: Mantener visible qué parte del repo es producto de ejemplo y qué parte es infraestructura metodológica.

## Reglas locales del repo
- MUST: Cualquier cambio Android futuro debe preservar bounded contexts y Clean Architecture por feature.
- MUST: Para cambios de producto Android, ejecutar el comando de validación documentado por el módulo afectado antes de cerrar la iteración.
