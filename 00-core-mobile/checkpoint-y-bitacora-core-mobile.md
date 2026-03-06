# Checkpoint y bitácora - Etapa 0: Core Mobile

Este documento cierra el bloque de fundamentos comunes del Mobile Architect. No sirve para memorizar teoría: sirve para comprobar si ya sabes leer, discutir y defender decisiones arquitectónicas antes de bajar al detalle de Android.

## Qué debes poder hacer antes de avanzar

- Explicar por qué una arquitectura móvil profesional necesita reglas de dependencia y no solo buenas intenciones.
- Distinguir claramente `Domain`, `Application`, `Interface` e `Infrastructure`.
- Leer un ADR corto y resumir por qué se eligió una opción y no otra.
- Explicar qué papel juegan observabilidad, rollback, seguridad y dependency governance en un equipo real.
- Entender la convención de flechas del curso y leer un diagrama sin confundir runtime, contrato, wiring y propagación.

## Checklist de cierre

- [ ] Puedo describir la semántica de las cuatro flechas del curso sin mirar la leyenda.
- [ ] Sé justificar por qué `Composition Root` no debe vivir repartido por el sistema.
- [ ] Entiendo la diferencia entre una restricción dura y una restricción blanda en una decisión técnica.
- [ ] Puedo explicar qué es un `quality gate` y por qué evita deuda invisible.
- [ ] Identifico al menos tres riesgos reales de operar una app móvil en producción.

## Mini-quiz de autoevaluación

1. ¿Qué problema aparece si una feature importa directamente otra feature para navegar?
2. ¿Por qué `rollback` y `feature flag` no resuelven exactamente el mismo tipo de riesgo?
3. ¿Qué evidencia mínima pedirías para aceptar una PR en un módulo crítico?
4. ¿Qué diferencia hay entre un puerto y una implementación concreta?
5. ¿Qué ventaja aporta documentar una decisión en un ADR aunque hoy parezca obvia?

## Evidencias mínimas

- Un resumen propio de una decisión arquitectónica del curso.
- Un diagrama leído y explicado con tus palabras.
- Una lista de tres smells arquitectónicos que ahora sabes detectar.

## Bitácora guiada

### Lo que ya domino

Escribe tres ideas que ya podrías explicar a otra persona sin leer apuntes.

### Lo que aún me cuesta

Anota qué parte del bloque te sigue pareciendo abstracta y qué ejemplo necesitas para aterrizarla.

### Decisión técnica que ahora veo con más claridad

Describe una decisión del bloque y explica qué trade-off te ayudó a entenderla.

### Riesgo que antes no veía

Anota un riesgo operativo o de arquitectura que antes te parecía “tema de seniors” y ahora sabes reconocer.

### Próximo paso

Define qué necesitas vigilar cuando entres en `Nivel Cero` para no construir sobre una base confusa.
