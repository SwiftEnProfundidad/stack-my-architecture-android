# Plan de sprint detallado — implementación del curso Android

## Objetivo del sprint

Ejecutar la construcción completa del curso y del proyecto Android real de forma incremental, verificable y pedagógicamente segura para nivel adolescente desde cero.

## Reglas de ejecución

1. Cada día termina con entregables concretos en el repositorio.
2. Ningún módulo nuevo se abre sin checklist de calidad del módulo anterior.
3. Cada bloque teórico debe tener práctica guiada y mini reto asociado.
4. Todo cambio técnico debe mantener compatibilidad con la matriz estable validada.
5. El contenido principal de cada lección debe redactarse en formato narrativo completo, paso a paso, con lenguaje apto para 14 años.
6. No se usarán listas con viñetas como formato principal de explicación conceptual.
7. Todo bloque de código debe explicarse en lenguaje natural línea por línea antes y después del ejemplo.
8. Cada lección debe anticipar dudas típicas de principiante y resolverlas en el propio texto.

---

## Semana 1 — Cimentación del repositorio y Nivel Cero

### Día 1 — Estructura base y contrato editorial

#### Archivos a crear primero

- `README.md`
- `00-informe/INFORME-CURSO.md`
- `00-informe/DECISIONES-TOMADAS.md`
- `00-informe/TODO.md`
- `00-nivel-cero/00-introduccion.md`
- `00-nivel-cero/00-setup.md`
- `anexos/glosario.md`

#### Entregables del día

- Índice raíz navegable del curso
- Convenciones de escritura pedagógica para estudiante de 14 años
- Checklist editorial por lección

#### Contenido exacto por archivo de Día 1

##### 1) `README.md`

Debe incluir exactamente estos bloques en este orden:

1. Título del curso Android
2. Manifiesto corto para estudiante de 14 años
3. Mapa de niveles: Nivel Cero, Junior, Midlevel, Senior, Maestría
4. Cómo estudiar el curso paso a paso
5. Reglas del alumno: practicar, equivocarse, corregir, documentar
6. Índice navegable hacia carpetas principales
7. Tabla de progreso rápido por nivel

Plantilla mínima esperada:

- sección `Objetivo del curso`
- sección `Ruta de aprendizaje`
- sección `Cómo usar este repositorio`
- sección `Requisitos técnicos`
- sección `Progreso y evaluación`

##### 2) `00-informe/INFORME-CURSO.md`

Debe definir el contrato pedagógico oficial:

1. Perfil de entrada y salida
2. Principios didácticos obligatorios
3. Definición de calidad de una lección
4. Matriz técnica estable validada
5. Sistema de evaluación y evidencias
6. Regla de actualización de versiones

Plantilla mínima esperada:

- `Resumen ejecutivo`
- `Objetivos medibles`
- `Métricas de éxito del curso`
- `Riesgos pedagógicos y mitigaciones`

##### 3) `00-informe/DECISIONES-TOMADAS.md`

Bitácora de decisiones arquitectónicas y curriculares.

Estructura exacta por registro:

- `ID`
- `Fecha`
- `Decisión`
- `Contexto`
- `Alternativas evaluadas`
- `Elección`
- `Impacto`
- `Acciones derivadas`

Debe iniciar con decisiones base:

- adopción de Nivel Cero
- adopción de stack Android validado
- adopción de progresión por niveles

##### 4) `00-informe/TODO.md`

Backlog operativo del curso.

Columnas obligatorias por item:

- `ID`
- `Nivel`
- `Tarea`
- `Estado`
- `Evidencia esperada`
- `Bloqueado por`

Debe iniciar con tareas del Día 1 y Día 2.

##### 5) `00-nivel-cero/00-introduccion.md`

Lección de arranque absoluto para quien no programa.

Estructura exacta:

1. Qué aprenderás hoy
2. Qué es programar explicado simple
3. Ejemplo cotidiano traducido a pasos
4. Mini práctica sin código
5. Mini práctica con pseudocódigo
6. Errores típicos del primer día
7. Comprobación de comprensión
8. Mini reto de 10 minutos
9. Solución guiada
10. Evidencia que debe entregar el alumno

##### 6) `00-nivel-cero/00-setup.md`

Guía de instalación ultra guiada y verificable.

Debe cubrir:

1. Requisitos de máquina explicados en lenguaje simple
2. Instalación Android Studio paso a paso
3. Configuración SDK 36
4. Verificación JDK 17
5. Primer proyecto que compila
6. Solución de errores frecuentes de setup
7. Checklist final de entorno listo

Cada paso debe incluir:

- objetivo del paso
- acción concreta
- resultado esperado
- qué hacer si falla

##### 7) `anexos/glosario.md`

Diccionario para adolescentes, términos simples.

Formato exacto por término:

- `Término`
- `Definición muy simple`
- `Ejemplo real`
- `Error común asociado`

Día 1 debe cerrar con al menos 30 términos base.

#### Criterio de aceptación de Día 1

El Día 1 queda aprobado solo si:

1. Los 7 archivos existen
2. Todos usan estructura pedagógica fija
3. Hay lenguaje accesible para 14 años
4. Existe checklist de evidencia por archivo
5. Queda listo el arranque del Día 2 sin ambigüedad

#### Plantillas exactas para escribir cada archivo de Día 1

##### Plantilla exacta de `README.md`

```md
# Stack My Architecture Android

## Manifiesto del curso

## Objetivo del curso

## Ruta de aprendizaje
- Nivel Cero
- Junior
- Midlevel
- Senior
- Maestría

## Cómo usar este repositorio

## Requisitos técnicos

## Índice principal
- 00-informe
- 00-nivel-cero
- 01-junior
- 02-midlevel
- 03-senior
- 04-maestria
- anexos
- proyecto-android

## Progreso y evaluación
| Nivel | Estado | Evidencia mínima |
|---|---|---|

## Reglas del estudiante
```

##### Plantilla exacta de `00-informe/INFORME-CURSO.md`

```md
# Informe del curso

## Resumen ejecutivo

## Perfil de entrada

## Perfil de salida

## Principios didácticos obligatorios

## Matriz técnica validada
| Componente | Versión | Fuente oficial |
|---|---|---|

## Sistema de evaluación

## Evidencias obligatorias por nivel

## Métricas de éxito del curso

## Riesgos pedagógicos y mitigaciones
```

##### Plantilla exacta de `00-informe/DECISIONES-TOMADAS.md`

```md
# Decisiones tomadas

## Registro ADR-EDU-001
- ID:
- Fecha:
- Decisión:
- Contexto:
- Alternativas evaluadas:
- Elección:
- Impacto:
- Acciones derivadas:

## Registro ADR-EDU-002
- ID:
- Fecha:
- Decisión:
- Contexto:
- Alternativas evaluadas:
- Elección:
- Impacto:
- Acciones derivadas:
```

##### Plantilla exacta de `00-informe/TODO.md`

```md
# Backlog operativo

| ID | Nivel | Tarea | Estado | Evidencia esperada | Bloqueado por |
|---|---|---|---|---|---|
| D1-01 | Día 1 | Crear README | Pendiente | README con índice completo | - |
| D1-02 | Día 1 | Crear informe curso | Pendiente | Informe con matriz técnica | D1-01 |
| D2-01 | Día 2 | Módulo Nivel Cero 01 | Pendiente | Lección + mini reto + solución | D1 completado |
```

##### Plantilla exacta de `00-nivel-cero/00-introduccion.md`

```md
# Nivel Cero · Introducción

## Qué aprenderás hoy

## Qué es programar explicado fácil

## Ejemplo de vida diaria convertido en pasos

## Mini práctica sin código

## Mini práctica con pseudocódigo

## Errores típicos del primer día

## Comprobación de comprensión

## Mini reto de 10 minutos

## Solución guiada

## Evidencia que debes entregar
```

##### Plantilla exacta de `00-nivel-cero/00-setup.md`

```md
# Nivel Cero · Setup

## Objetivo del setup

## Requisitos mínimos de equipo

## Paso 1 · Instalar Android Studio
- Acción
- Resultado esperado
- Si falla

## Paso 2 · Configurar SDK 36
- Acción
- Resultado esperado
- Si falla

## Paso 3 · Verificar JDK 17
- Acción
- Resultado esperado
- Si falla

## Paso 4 · Crear y ejecutar primer proyecto
- Acción
- Resultado esperado
- Si falla

## Errores frecuentes de instalación

## Checklist final de entorno listo
```

##### Plantilla exacta de `anexos/glosario.md`

```md
# Glosario base

## Término 01
- Término:
- Definición muy simple:
- Ejemplo real:
- Error común asociado:

## Término 02
- Término:
- Definición muy simple:
- Ejemplo real:
- Error común asociado:
```

---

### Día 2 — Nivel Cero módulos 1 a 4

#### Archivos

- `00-nivel-cero/01-que-es-software.md`
- `00-nivel-cero/02-logica-basica.md`
- `00-nivel-cero/03-primer-kotlin.md`
- `00-nivel-cero/04-variables-y-tipos.md`

#### Entregables

- Lecciones con ejemplos ultra simples
- Sección fija de errores comunes por módulo
- Mini retos con solución en cada archivo

---

### Día 3 — Nivel Cero módulos 5 a 8

#### Archivos

- `00-nivel-cero/05-condicionales-y-bucles.md`
- `00-nivel-cero/06-funciones.md`
- `00-nivel-cero/07-errores-frecuentes.md`
- `00-nivel-cero/08-android-studio-desde-cero.md`

#### Entregables

- Primer bloque completo de lógica computacional
- Guía práctica de Android Studio desde instalación hasta primer run

---

### Día 4 — Nivel Cero módulos 9 a 12 y proyecto integrador

#### Archivos

- `00-nivel-cero/09-primera-app-compose.md`
- `00-nivel-cero/10-inputs-y-validacion.md`
- `00-nivel-cero/11-navegacion-simple.md`
- `00-nivel-cero/12-proyecto-rutina-diaria.md`
- `00-nivel-cero/entregables-nivel-cero.md`

#### Entregables

- Nivel Cero completo
- Rúbrica de paso Nivel Cero → Junior
- Evidencias exigidas para habilitar siguiente fase

---

### Día 5 — Scaffold técnico del proyecto Android

#### Estructura a crear

- `proyecto-android/`
- `proyecto-android/settings.gradle.kts`
- `proyecto-android/build.gradle.kts`
- `proyecto-android/gradle.properties`
- `proyecto-android/gradle/libs.versions.toml`
- `proyecto-android/app/`
- `proyecto-android/core/common/`
- `proyecto-android/core/ui/`
- `proyecto-android/core/testing/`

#### Entregables

- Proyecto compila en limpio
- Matriz de versiones aplicada en catálogo de versiones
- README técnico de arranque local

---

## Semana 2 — Fase Junior completa

### Día 6 — Junior base didáctica

#### Archivos

- `01-junior/00-introduccion.md`
- `01-junior/01-kotlin-aplicado.md`
- `01-junior/02-compose-intermedio.md`
- `01-junior/03-estado-local-vs-pantalla.md`

#### Entregables

- Fundamentos Junior listos y encadenados con Nivel Cero

---

### Día 7 — UDF + ViewModel + estructura limpia

#### Archivos

- `01-junior/04-viewmodel-y-udf.md`
- `01-junior/05-estructura-proyecto-limpia.md`
- `01-junior/06-validacion-formularios.md`

#### Entregables

- Primera feature guiada con UDF
- Checklist de smells de estado y validación

---

### Día 8 — Testing introductorio + errores

#### Archivos

- `01-junior/07-testing-unitario-intro.md`
- `01-junior/08-manejo-errores-usuario.md`
- `01-junior/09-proyecto-integrador-junior.md`
- `01-junior/entregables-junior.md`

#### Entregables

- Proyecto integrador Junior
- Criterio de paso Junior → Midlevel

---

### Día 9 — Implementación técnica feature Junior en código

#### Código objetivo

- `proyecto-android/feature/onboarding/`
- `proyecto-android/feature/auth/`
- pruebas unitarias asociadas

#### Entregables

- Feature real operativa
- Tests básicos ejecutando

---

### Día 10 — Buffer de consolidación

#### Entregables

- Cierre de huecos detectados
- Revisión transversal de coherencia pedagógica y técnica

---

## Semana 3 — Midlevel end-to-end

### Día 11

- `02-midlevel/00-introduccion.md`
- `02-midlevel/01-arquitectura-android-recomendada.md`
- `02-midlevel/02-repositorios-y-contratos.md`

### Día 12

- `02-midlevel/03-coroutines-flow-reales.md`
- `02-midlevel/04-lifecycle-aware-collection.md`
- `02-midlevel/05-room-modelado.md`

### Día 13

- `02-midlevel/06-datastore.md`
- `02-midlevel/07-api-real-red.md`
- `02-midlevel/08-offline-first-sincronizacion.md`

### Día 14

- `02-midlevel/09-navegacion-moderna.md`
- `02-midlevel/10-pruebas-integracion.md`
- `02-midlevel/11-proyecto-integrador-midlevel.md`
- `02-midlevel/entregables-midlevel.md`

### Día 15

- Implementación técnica real en `feature/catalog`
- integración Room + DataStore + red

---

## Semana 4 — Senior y plataforma de calidad

### Día 16

- `03-senior/00-introduccion.md`
- `03-senior/01-modularizacion-feature-first.md`
- `03-senior/02-hilt-avanzado.md`

### Día 17

- `03-senior/03-workmanager.md`
- `03-senior/04-observabilidad-basica.md`
- `03-senior/05-resiliencia-reintentos.md`

### Día 18

- `03-senior/06-compose-ui-testing-avanzado.md`
- `03-senior/07-debugging-sistematico.md`
- `03-senior/08-performance-compose.md`

### Día 19

- `03-senior/09-macrobenchmark.md`
- `03-senior/10-baseline-profiles.md`
- `03-senior/11-proyecto-integrador-senior.md`
- `03-senior/entregables-senior.md`

### Día 20

- Implementación módulos `benchmark/` y `baselineprofile/`
- quality gates iniciales de CI

---

## Semana 5 — Maestría, release y cierre

### Día 21

- `04-maestria/00-introduccion.md`
- `04-maestria/01-arquitectura-evolutiva.md`
- `04-maestria/02-gobernanza-tecnica.md`

### Día 22

- `04-maestria/03-calidad-end-to-end.md`
- `04-maestria/04-seguridad-android.md`
- `04-maestria/05-accesibilidad-avanzada.md`

### Día 23

- `04-maestria/06-ci-cd.md`
- `04-maestria/07-mantenimiento-documentacion.md`
- `04-maestria/08-release-play-store.md`

### Día 24

- `04-maestria/09-proyecto-final.md`
- `04-maestria/10-defensa-tecnica.md`
- `04-maestria/entregables-maestria.md`

### Día 25 — Cierre integral

#### Entregables finales

- Revisión de consistencia total del curso
- Auditoría de enlaces internos
- Validación de build y tests
- Informe de cierre y siguientes iteraciones

---

## Checklist diario de definición de terminado

1. Archivos previstos del día creados
2. Lecciones con lenguaje accesible y progresivo
3. Práctica guiada + mini reto + solución incluidos
4. Errores comunes documentados
5. Evidencias de aprendizaje definidas
6. Coherencia con matriz técnica validada
7. Estado actualizado en `00-informe/TODO.md`

---

## Riesgos y mitigación

1. Sobrecarga cognitiva del estudiante
   - Mitigación: microbloques + recapitulaciones + refuerzo
2. Deriva técnica por cambios de versión
   - Mitigación: control de matriz y ADR de cambios
3. Desalineación entre teoría y código real
   - Mitigación: cada módulo teórico enlaza a código verificable
4. Falta de criterios claros de paso
   - Mitigación: rúbricas y evidencias por fase obligatorias

---

## Resultado esperado al finalizar el sprint

- Curso Android completo y ejecutable en entorno educativo real
- Ruta de aprendizaje desde cero absoluto hasta maestría
- Proyecto Android profesional verificable con estándares modernos
- Material listo para implementación en modo Code sin ambigüedad
