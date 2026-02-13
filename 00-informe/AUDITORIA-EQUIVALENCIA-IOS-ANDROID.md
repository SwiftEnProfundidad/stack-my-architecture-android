# Auditoría de equivalencia iOS ↔ Android

## Contexto y objetivo de esta auditoría

Este documento existe para responder una pregunta incómoda, pero necesaria: si una persona termina el recorrido Android, ¿sale con el mismo nivel de preparación profesional que quien termina el recorrido iOS? La respuesta, en el estado actual, es que todavía no. Hay avances importantes en cobertura y narrativa, pero la equivalencia real exige algo más que contenido amplio. Exige evidencia operativa consistente, un proyecto final verdaderamente integrador y una forma de evaluación que compruebe empleabilidad técnica, no solo comprensión conceptual.

La comparación se hace sobre artefactos concretos de ambos repositorios. Del lado Android se toma como referencia la estructura y el contrato pedagógico publicado, y del lado iOS se toma el estándar de profundidad operativa ya consolidado.

## Estado comparativo actual

Cuando se compara la propuesta de valor, Android ya tiene una promesa formativa potente: progresión clara, stack moderno y cobertura por niveles. Esa base está bien representada en [`README.md`](../README.md) y en [`INFORME-CURSO.md`](INFORME-CURSO.md). Sin embargo, la versión iOS sigue mostrando una columna vertebral más cerrada entre teoría, decisiones y ejecución verificable, visible en [`README.md`](../../stack-my-architecture-ios/README.md) y en su informe fundacional [`INFORME-CURSO.md`](../../stack-my-architecture-ios/00-informe/INFORME-CURSO.md).

En profundidad técnica, Android cubre casi todos los temas críticos del stack solicitado, pero todavía no obliga al alumno a demostrarlos de forma integrada sobre un único producto vivo con gates duros de calidad. En iOS esa exigencia aparece con más fuerza en la continuidad de sus etapas y artefactos.

En coherencia pedagógica, Android mejoró tras revisiones de calidad, pero aún hay brechas de trazabilidad entre lo que se aprende en módulos aislados y lo que debe sostenerse en un ciclo real de release, operación y mantenimiento de producto.

## Brechas críticas detectadas

La primera brecha es estructural: el proyecto final existe como anexo útil, pero no funciona todavía como hilo conductor obligatorio de extremo a extremo. Eso deja espacio para completar niveles con buen conocimiento parcial sin haber demostrado integración profesional completa.

La segunda brecha es de evidencia técnica. Faltan criterios de aceptación duros que conecten cada nivel con resultados verificables en build, tests, rendimiento, observabilidad, release y mantenimiento.

La tercera brecha es de evaluación de empleabilidad. Hay entregables por nivel, pero falta una rúbrica unificada que convierta esas entregas en una señal clara de readiness profesional.

La cuarta brecha es de gobernanza de decisiones. Android necesita reforzar el uso de decisiones técnicas versionadas para que la evolución del proyecto final no dependa de memoria ni criterio implícito.

## Criterio de equivalencia objetivo

Se considera equivalencia real con iOS solo si Android cumple simultáneamente estas condiciones:

1) El proyecto final no es accesorio, sino obligatorio y transversal a todo el recorrido.
2) Cada nivel deja evidencia técnica verificable en código, pruebas, rendimiento y operación.
3) Existe rúbrica de empleabilidad única con umbrales explícitos de aprobación.
4) Las decisiones arquitectónicas relevantes quedan registradas y defendibles.
5) El cierre incluye simulación realista de trabajo en equipo, release y mantenimiento post-publicación.

## Decisión de esta auditoría

La auditoría concluye que el curso Android debe entrar en fase de refuerzo controlado. El objetivo no es reescribir todo ni romper continuidad. El objetivo es convertir lo ya construido en un sistema de formación verificable por evidencias, con un proyecto final central y una evaluación que realmente mida desempeño profesional.

La implementación de esta decisión se desarrolla en el plan de refuerzo y en el nuevo bloque de proyecto final.
