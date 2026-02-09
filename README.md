# Stack My Architecture Android

Curso práctico para aprender Android desde cero absoluto (14 años) hasta maestría técnica, con una ruta clara, progresiva y orientada a proyectos reales.

## Core Mobile (iOS + Android)

This is a Mobile Architecture framework: iOS depth + Android parity via shared decision-making, quality, operations, and governance.

- [Core Mobile: Introducción](00-core-mobile/00-introduccion.md)
- [Core Mobile: Crosswalk iOS ↔ Android](00-core-mobile/11-crosswalk-ios-android.md)

## Manifiesto del curso

Aquí no se aprende memorizando pantallas: se aprende **entendiendo**, **practicando**, **equivocándose** y **corrigiendo**.

## Objetivo del curso

Que puedas construir apps Android reales con buenas prácticas profesionales, aunque hoy no sepas programar.

## Ruta de aprendizaje

- Nivel Cero
- Junior
- Midlevel
- Senior
- Maestría

## Cómo usar este repositorio

1. Sigue el orden de carpetas por nivel.
2. En cada lección: lee, practica, haz el mini reto y revisa la solución.
3. Guarda evidencias de progreso (capturas, código y respuestas cortas).
4. No avances de nivel si no cumples la rúbrica del nivel actual.

## Estudio en HTML local (modo lectura cómoda)

El curso Android ya incluye generación HTML y arranque local con doble clic, igual que el flujo de iOS.

Si quieres abrirlo con un solo gesto, usa [`open-course.command`](../stack-my-architecture-android/open-course.command). Ese comando genera el HTML completo y levanta localhost automáticamente en tu navegador.

También puedes lanzarlo por terminal con [`scripts/open-course.command`](../stack-my-architecture-android/scripts/open-course.command). El generador que transforma Markdown en HTML está en [`scripts/build-html.py`](../stack-my-architecture-android/scripts/build-html.py) y deja el resultado en `dist/curso-stack-my-architecture-android.html`.

## HTML Hub

Puedes abrir iOS + Android desde un único portal HTML en `../stack-my-architecture-hub/index.html`.

1. Ejecuta `../stack-my-architecture-hub/scripts/build-hub.sh`
2. Abre `../stack-my-architecture-hub/index.html`
3. Cambia de curso con el menú burger **Course Switcher** dentro del HTML

Study UX se mantiene por curso (aislado por `course-id`):

- iOS: `stack-my-architecture-ios`
- Android: `stack-my-architecture-android`

## Requisitos técnicos

- Android Studio estable
- JDK 17
- Android SDK 36
- Kotlin 2.3.10
- AGP 9.0.0
- Gradle 9.1.0

## Índice principal

- `00-informe`
- `00-core-mobile`
- `00-nivel-cero`
- `01-junior`
- `02-midlevel`
- `03-senior`
- `04-maestria`
- `05-proyecto-final`
- `anexos`
- `proyecto-android`
- `plans`

## Avance real por nivel (módulos publicados)

### Nivel Cero

- `00-introduccion.md`
- `00-setup.md`
- `01-que-es-software.md`
- `02-logica-basica.md`
- `03-primer-kotlin.md`
- `04-variables-y-tipos.md`
- `05-condicionales-y-bucles.md`
- `06-funciones.md`
- `07-errores-frecuentes.md`
- `08-android-studio-desde-cero.md`
- `09-primera-app-compose.md`
- `10-inputs-y-validacion.md`
- `11-navegacion-simple.md`
- `12-proyecto-rutina-diaria.md`
- `entregables-nivel-cero.md`

### Junior

- `00-introduccion.md`
- `00-setup-junior.md`
- `01-arquitectura-android-recomendada.md`
- `02-feature-base-practica.md`
- `03-navegacion-moderna-navigation-compose.md`
- `04-hilt-integracion-inicial.md`
- `05-room-offline-first.md`
- `06-datastore-estado-ligero.md`
- `07-workmanager-tareas-persistentes.md`
- `08-compose-ui-testing.md`
- `09-pruebas-unitarias-viewmodel-repositorio.md`
- `entregables-nivel-junior.md`

### Midlevel

- `00-introduccion.md`
- `01-red-robusta-retrofit-okhttp.md`
- `02-offline-first-sincronizacion.md`
- `03-consistencia-y-resolucion-de-conflictos.md`
- `04-observabilidad-y-diagnostico.md`
- `05-pruebas-de-integracion-offline-sync.md`
- `06-quality-gates-ci-offline-sync.md`
- `07-performance-ci-macrobenchmark-baselineprofiles.md`
- `08-observabilidad-produccion-metricas-alertas.md`
- `09-decisiones-evolutivas-con-metricas.md`
- `10-gobernanza-dependencias-entre-features.md`
- `11-versionado-contratos-internos.md`
- `12-evolucion-navegacion-y-deeplinks-compatibles.md`

### Senior

- `00-introduccion.md`
- `01-release-strategy-y-rollback-seguro.md`
- `02-incident-response-y-runbooks-operativos.md`
- `03-slos-error-budgets-priorizacion-fiabilidad.md`
- `04-tablero-operativo-fiabilidad-y-alertas-accionables.md`
- `05-gobernanza-tecnica-de-sprint-fiabilidad-vs-roadmap.md`
- `06-simulacion-sprint-bajo-presion-roadmap-y-fiabilidad.md`
- `07-cierre-del-bloque-senior-y-transicion-a-maestria.md`

### Maestría

- `00-introduccion.md`
- `01-contratos-evolutivos-entre-dominios.md`
- `02-bounded-contexts-y-ownership-tecnico.md`
- `03-mapa-de-dependencias-y-acoplamiento-circular.md`
- `04-migraciones-transversales-sin-bloqueo.md`
- `05-coordinacion-release-rollback-y-comunicacion-tecnica.md`
- `06-evolucion-multi-equipo-y-gobernanza-trimestral.md`
- `07-defensa-tecnica-del-proyecto-android.md`
- `08-cierre-proyecto-final-y-publicacion-play-store.md`
- `09-rubrica-final-y-entrevista-tecnica-android.md`
- `10-plan-de-90-dias-despues-del-curso.md`
- `11-epilogo-profesional-y-siguientes-retos.md`
- `12-casos-reales-y-antipatrones-de-equipos-android.md`
- `13-operacion-largo-plazo-y-deuda-tecnica.md`
- `14-primer-ano-en-equipo-android-real.md`
- `15-mapa-de-carrera-android-de-junior-a-senior.md`
- `16-cierre-definitivo-del-recorrido-android.md`

### Proyecto final integrador

- `05-proyecto-final/00-brief.md`
- `05-proyecto-final/00-brief-ruralgo-fieldops.md`
- `05-proyecto-final/01-rubrica-empleabilidad.md`
- `05-proyecto-final/02-evidencias-obligatorias.md`
- `05-proyecto-final/03-operacion-senior.md`
- `05-proyecto-final/04-gobernanza-maestria.md`

### Entregables reforzados por nivel

- `01-junior/entregables-nivel-junior.md`
- `02-midlevel/entregables-nivel-midlevel.md`

## Control de calidad pedagógica

El estado de auditoría y mejora continua de las lecciones avanzadas se registra en `00-informe/REVISION-PEDAGOGICA.md` para mantener trazabilidad de brechas detectadas y reescrituras aplicadas.

## Refuerzo de equivalencia con iOS

La auditoría de brechas y la propuesta reforzada de implementación se documentan en [`00-informe/AUDITORIA-EQUIVALENCIA-IOS-ANDROID.md`](../stack-my-architecture-android/00-informe/AUDITORIA-EQUIVALENCIA-IOS-ANDROID.md), [`00-informe/PLAN-REFUERZO-CURSO-ANDROID.md`](../stack-my-architecture-android/00-informe/PLAN-REFUERZO-CURSO-ANDROID.md) y [`00-informe/MEJORAS-POR-MODULO-Y-EVIDENCIAS.md`](../stack-my-architecture-android/00-informe/MEJORAS-POR-MODULO-Y-EVIDENCIAS.md).

## Progreso y evaluación

| Nivel | Estado | Evidencia mínima |
|---|---|---|
| Nivel Cero | Completado | Mini app funcional + checklist completado |
| Junior | Completado | Feature con ViewModel + pruebas básicas |
| Midlevel | Completado | Integración red + Room + DataStore |
| Senior | Completado | Gobernanza operativa, SLOs y respuesta a incidentes aplicados |
| Maestría | Completado | Gobernanza de escala, defensa técnica, publicación y plan profesional post-curso |

## Reglas del estudiante

1. Practica todos los días, aunque sea poco.
2. Si algo falla, escribe qué pasó antes de pedir ayuda.
3. No copies sin entender.
4. Explica con tus palabras lo que aprendiste.
5. Cada error corregido es progreso real.

## Cierre de recorrido

El curso queda cerrado en contenido con una ruta completa desde fundamentos hasta operación y criterio profesional de Android en contexto real. La continuidad recomendada está descrita en [`04-maestria/10-plan-de-90-dias-despues-del-curso.md`](../stack-my-architecture-android/04-maestria/10-plan-de-90-dias-despues-del-curso.md), en [`04-maestria/11-epilogo-profesional-y-siguientes-retos.md`](../stack-my-architecture-android/04-maestria/11-epilogo-profesional-y-siguientes-retos.md) y en el cierre global de entrega [`00-informe/CIERRE-FINAL-CURSO.md`](../stack-my-architecture-android/00-informe/CIERRE-FINAL-CURSO.md).
