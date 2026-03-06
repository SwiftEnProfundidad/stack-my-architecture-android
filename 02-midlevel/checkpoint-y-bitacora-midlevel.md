# Checkpoint y bitácora - Etapa 2: Midlevel

Midlevel valida que tu sistema se mantiene en pie cuando aparecen fricción real, red inestable, conflictos y necesidad de evidencia técnica. Aquí ya no basta con que “funcione en demo”.

## Qué debes poder hacer antes de avanzar

- Diseñar un flujo `offline-first` con sincronización entendible.
- Probar integración entre red, persistencia y repositorio con escenarios reales de fallo.
- Instrumentar observabilidad mínima para diagnosticar sync, conflictos y recuperación.
- Establecer un baseline de rendimiento y razonar a partir de datos.
- Subir quality gates al pipeline sin romper la capacidad de iterar.

## Checklist de cierre

- [ ] Mi flujo principal soporta pérdida de red sin volverse incoherente.
- [ ] Tengo pruebas que cubren lectura, escritura, sync y conflictos básicos.
- [ ] Sé explicar cómo diagnosticaría una sincronización fallida en producción.
- [ ] Tengo un baseline inicial de rendimiento y una acción concreta derivada de él.
- [ ] El pipeline detecta roturas de flujos críticos antes del merge.

## Mini-quiz de autoevaluación

1. ¿Qué diferencia hay entre cachear lectura y ser realmente `offline-first`?
2. ¿Qué evidencia te dice que un conflicto de sincronización está bien resuelto?
3. ¿Por qué un log sin contexto útil no es observabilidad real?
4. ¿Qué valor tiene un baseline si nadie lo consulta al evolucionar el sistema?
5. ¿Qué quality gate pondrías primero si solo pudieras elegir uno?

## Evidencias mínimas

- Flujo `offline-first` demostrable.
- Tests de integración o end-to-end técnico de sync.
- Métricas o logs útiles para diagnóstico.
- Pipeline con al menos un gate crítico automatizado.

## Bitácora guiada

### Lo que ya domino

Anota qué parte de `offline-first` ya entiendes con seguridad: lectura, escritura, sincronización o consistencia.

### Lo que aún me cuesta

Describe el punto donde el sistema empieza a sentirse “más grande que tú” y qué necesitas para volverlo entendible.

### Decisión técnica mejor defendida

Explica una decisión de consistencia, conflictos u observabilidad que ahora sabes justificar.

### Riesgo operativo detectado

Anota un fallo que podría aparecer en producción y cómo lo vigilarías.

### Próximo paso

Escribe qué disciplina necesitas para entrar en Senior pensando ya en fiabilidad y operación, no solo en implementación.
