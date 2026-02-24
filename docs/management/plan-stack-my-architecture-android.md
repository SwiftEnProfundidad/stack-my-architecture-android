# Rediseño curricular integral — Stack My Architecture Android

## 0) Propósito del rediseño

Diseñar una ruta **completa, progresiva y ejecutable** para una persona de 14 años que empieza desde cero absoluto, hasta lograr dominio equivalente a maestría técnica junior/semisenior avanzada en Android.

Este plan está preparado para implementación real en el repositorio `stack-my-architecture-android`.

---

## 1) Principios pedagógicos obligatorios

1. **Primero entender, luego memorizar, luego crear**
2. **De lo concreto a lo abstracto**
3. **Un concepto nuevo por bloque práctico**
4. **Repetición espaciada y recapitulación frecuente**
5. **Evaluación por evidencias observables, no por intuición**
6. **Errores como parte del aprendizaje con corrección guiada**
7. **Escalado gradual de dificultad sin saltos bruscos**

---

## 2) Perfil de entrada y perfil de salida

### Perfil de entrada

- 14 años
- Sin base previa en programación
- Sin conocimientos de Android Studio, terminal, Git, arquitectura ni testing

### Perfil de salida

Capaz de construir y mantener apps Android reales con:

- Kotlin moderno
- UI en Jetpack Compose
- Arquitectura recomendada Android
- Manejo de estado con UDF + ViewModel
- Persistencia offline-first con Room y DataStore
- Concurrencia con Coroutines y Flow lifecycle-aware
- Calidad con tests, debugging, benchmark y baseline profiles
- Documentación, CI/CD y guía de publicación en Play Store

---

## 3) Matriz técnica estable validada

| Componente | Versión base del curso | Política |
|---|---:|---|
| Kotlin | 2.3.10 | Fijada en baseline |
| AGP | 9.0.0 | Fijada en baseline |
| Gradle | 9.1.0 | Compatible con AGP 9.0.0 |
| JDK | 17 | Requerido |
| compileSdk | 36 | Requerido |
| targetSdk | 36 | Requerido |
| Compose BOM | 2026.01.01 | Controlado por BOM |
| Navigation Compose | 2.9.6 | Compatible con BOM/base |
| Hilt | estable oficial compatible | Sin versiones huérfanas |
| Room | estable oficial compatible | Offline-first obligatorio |
| DataStore | estable oficial compatible | Preferencias/estado pequeño |
| WorkManager | estable oficial compatible | Tareas persistentes |

### Regla de actualización

Si cambia una versión estable oficial durante implementación:

1. Actualizar matriz
2. Registrar decisión en informe
3. Explicar impacto en lecciones
4. Ajustar ejercicios y proyectos afectados

---

## 4) Estructura macro de niveles

Se agrega explícitamente **Nivel Cero** antes de Junior:

1. **Nivel Cero** — Alfabetización tecnológica y lógica básica
2. **Junior** — Construcción guiada de apps simples funcionales
3. **Midlevel** — Integración entre capas, datos reales y arquitectura sólida
4. **Senior** — Resiliencia, escalabilidad, mantenibilidad, rendimiento
5. **Maestría** — Dominio técnico integral, criterio arquitectónico y calidad avanzada

---

## 5) Objetivos, competencias y criterios de paso por nivel

## Nivel Cero

### Objetivo

Construir bases mentales y operativas sin asumir conocimiento previo.

### Competencias esperadas

- Explicar qué es un programa
- Usar Android Studio de forma básica
- Comprender variables, decisiones, ciclos y funciones simples
- Ejecutar una app mínima y modificar texto/botones

### Criterio para pasar a Junior

Debe completar una mini app de hábitos diaria con:

- 3 pantallas básicas
- Navegación simple
- Estado local mínimo
- Entrega documentada de qué aprendió y qué errores corrigió

## Junior

### Objetivo

Crear apps funcionales con estructura inicial profesional.

### Competencias esperadas

- Kotlin intermedio inicial
- Compose y componentes reutilizables
- ViewModel por pantalla
- UDF básico
- Tests unitarios introductorios

### Criterio para pasar a Midlevel

Proyecto integrador fase Junior funcionando con:

- Feature de autenticación mockeada y luego real
- Estado bien modelado
- Errores de usuario controlados
- Cobertura mínima de pruebas definida

## Midlevel

### Objetivo

Integrar arquitectura recomendada Android con datos reales y persistencia.

### Competencias esperadas

- Capas UI/Data y Domain opcional coherente
- Repositorios
- Room + DataStore
- Consumo de API real
- Flow lifecycle-aware

### Criterio para pasar a Senior

Proyecto de catálogo con:

- Sincronización red + cache local
- Estrategia offline-first
- Pruebas de integración e instrumentadas
- Decisiones técnicas justificadas

## Senior

### Objetivo

Mejorar resiliencia, observabilidad, rendimiento y gobernanza técnica.

### Competencias esperadas

- WorkManager en tareas reales
- Manejo robusto de errores y reintentos
- Calidad por quality gates
- Macrobenchmark y Baseline Profiles
- Modularización feature-first

### Criterio para pasar a Maestría

Sistema multi-feature estable con:

- Métricas de rendimiento
- Pruebas completas por capa
- Documentación técnica mantenible
- CI con validaciones automatizadas

## Maestría

### Objetivo

Consolidar criterio arquitectónico y ejecución profesional de extremo a extremo.

### Competencias esperadas

- Diseñar arquitectura evolutiva
- Resolver trade-offs con evidencia
- Liderar decisiones de calidad y mantenibilidad
- Entregar producto listo para release

### Criterio de finalización

Proyecto final con:

- App Android completa en producción educativa
- Observabilidad y rendimiento medidos
- Plan de publicación Play Store
- Defensa técnica de decisiones

---

## 6) Malla curricular detallada por nivel

## Nivel Cero — 12 módulos

1. Qué es software y cómo piensa una app
2. Lógica diaria traducida a algoritmos
3. Primer contacto con Kotlin sin Android
4. Variables, tipos, operadores
5. Condicionales y bucles
6. Funciones y descomposición de problemas
7. Errores comunes de principiantes
8. Android Studio desde cero
9. Tu primera app Compose
10. Entradas de usuario y validación básica
11. Navegación muy simple entre pantallas
12. Mini proyecto Nivel Cero

### Dinámica por módulo

- Explicación breve y cercana
- Demostración guiada
- Práctica paso a paso
- Mini reto de 10 a 20 minutos
- Revisión de errores frecuentes
- Ticket de progreso

## Junior — 10 módulos

1. Kotlin aplicado a app real
2. Compose intermedio inicial
3. Estado local vs estado de pantalla
4. ViewModel y UDF desde cero
5. Estructura de proyecto limpia
6. Validación de formularios
7. Introducción a testing unitario
8. Manejo de errores y mensajes de usuario
9. Proyecto integrador Junior
10. Evaluación y readiness Midlevel

## Midlevel — 12 módulos

1. Arquitectura recomendada Android en profundidad
2. Repositorios y contratos
3. Coroutines y Flow en casos reales
4. lifecycle-aware collection
5. Room y modelado de entidades
6. DataStore para configuración persistente
7. API real y capa de red
8. Offline-first y sincronización
9. Navegación moderna robusta
10. Pruebas de integración
11. Proyecto integrador Midlevel
12. Evaluación y readiness Senior

## Senior — 12 módulos

1. Modularización feature-first
2. Hilt avanzado y composición
3. WorkManager para tareas persistentes
4. Observabilidad básica útil
5. Estrategias de resiliencia
6. Compose UI testing avanzado
7. Depuración sistemática
8. Performance en Compose
9. Macrobenchmark
10. Baseline Profiles
11. Proyecto integrador Senior
12. Evaluación y readiness Maestría

## Maestría — 10 módulos

1. Arquitectura evolutiva y trade-offs
2. Gobernanza técnica y convenciones
3. Estrategia de calidad de extremo a extremo
4. Seguridad aplicada en apps Android
5. Accesibilidad avanzada
6. CI/CD realista para equipo
7. Mantenimiento y documentación viva
8. Preparación release Play Store
9. Proyecto final de maestría
10. Defensa técnica final

---

## 7) Sistema de práctica y evaluación continua

## Estructura fija por lección

1. Qué aprenderás
2. Explicación conceptual simple
3. Práctica guiada paso a paso
4. Mini reto
5. Errores comunes y cómo corregir
6. Comprobación de comprensión
7. Evidencia de progreso

## Tipos de evaluación

- Diagnóstica al inicio de cada fase
- Formativa en cada módulo
- Sumativa por proyecto integrador
- Hito de paso entre niveles

## Evidencias exigidas

- Código funcional
- Tests ejecutables
- Bitácora de aprendizaje
- Checklist de calidad completado
- Breve justificación técnica de decisiones

---

## 8) Proyectos integradores por fase

1. **Nivel Cero**: App de Rutina Diaria
2. **Junior**: App de Tareas Personales con estado de pantalla
3. **Midlevel**: App Catálogo con Room + red + offline-first
4. **Senior**: App multi-feature con WorkManager + observabilidad + benchmark
5. **Maestría**: Producto final listo para publicación educativa

Cada proyecto incluye:

- enunciado
- guía paso a paso
- rúbrica
- solución de referencia
- extensión opcional de mayor dificultad

---

## 9) Errores frecuentes del principiante y estrategia de corrección

### Categorías principales

- Problemas de entorno y herramientas
- Confusión de tipos y nullabilidad
- Mal manejo del estado UI
- Dependencias mal configuradas
- Falta de separación por capas
- Pruebas inexistentes o frágiles

### Método de corrección

1. Detectar síntoma
2. Explicar causa en lenguaje simple
3. Corregir en pequeño
4. Repetir ejercicio corto de fijación
5. Registrar aprendizaje en bitácora

---

## 10) Estructura de repositorio objetivo

```text
stack-my-architecture-android/
  README.md
  00-informe/
  00-nivel-cero/
  01-junior/
  02-midlevel/
  03-senior/
  04-maestria/
  anexos/
  plans/
  proyecto-android/
```

Y en `proyecto-android/`:

```text
proyecto-android/
  app/
  core/
    common/
    ui/
    testing/
    network/
    database/
    datastore/
  feature/
    onboarding/
    auth/
    catalog/
    tasks/
  benchmark/
  baselineprofile/
```

---

## 11) Quality gates educativos y técnicos

No se avanza de fase si no se cumple:

1. Proyecto de fase funcional
2. Pruebas mínimas requeridas
3. Checklist de calidad completado
4. Explicación verbal o escrita de decisiones clave
5. Evidencias subidas al repositorio

---

## 12) Definición de terminado del rediseño

Este rediseño se considera listo para implementación cuando:

1. Nivel Cero está completamente integrado en la ruta
2. Existen objetivos, competencias y criterios de paso por cada nivel
3. La malla curricular detallada evita saltos de dificultad
4. Están definidos proyectos, rúbricas y evidencias
5. Hay estrategia explícita para errores comunes
6. La matriz técnica está establecida y controlada
7. La estructura del repositorio está preparada para producción educativa real

