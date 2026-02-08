# Esquema detallado · 02-midlevel/02-offline-first-sincronizacion.md

## Objetivo pedagógico del módulo

Este módulo enseñará a diseñar e implementar una estrategia offline-first real en Android, manteniendo continuidad con lo aprendido en Room, DataStore, WorkManager y capa de red robusta.

La lección se redactará con patrón narrativo continuo, con términos definidos en el momento de uso, y con todo bloque de código explicado línea por línea.

## Resultado de aprendizaje esperado

Al terminar el módulo, el estudiante podrá explicar y construir un flujo donde la app:

1. Lee primero desde almacenamiento local para mantener experiencia estable.
2. Sincroniza con remoto de forma segura y controlada.
3. Persiste cambios localmente con metadatos de sincronización.
4. Resuelve conflictos simples de datos sin romper consistencia.
5. Expone estado de sincronización a la UI de manera clara.

## Dependencias didácticas previas que se conectarán explícitamente

Se abrirá el módulo conectando con:

- `01-junior/05-room-offline-first.md` para base local.
- `01-junior/06-datastore-estado-ligero.md` para flags y preferencias ligeras.
- `01-junior/07-workmanager-tareas-persistentes.md` para sincronización diferida.
- `02-midlevel/01-red-robusta-retrofit-okhttp.md` para capa remota y contratos de error.

## Estructura pedagógica propuesta (secciones del módulo)

### 0) Introducción narrativa del problema real

Se explicará por qué “offline-first” no significa solo cachear, sino definir una política de verdad de datos.

Se presentará una metáfora simple para principiantes: libreta local y oficina central remota.

### 1) Definiciones mínimas antes de código

Se definirán, en el momento, términos como:

- Single source of truth.
- Sync state.
- Pending writes.
- Last sync timestamp.
- Conflict resolution.

Cada término tendrá: qué es, para qué sirve, por qué se usa aquí y qué pasaría sin él.

### 2) Diagrama de arquitectura de sincronización

Se incluirá Mermaid con etiquetas seguras (sin símbolos conflictivos), mostrando flujo:

UI → ViewModel → Repository → Local/Remote → SyncOrchestrator.

Se añadirá lectura guiada del diagrama en lenguaje simple.

### 3) Modelo de datos para sincronización

Se introducirán campos nuevos en `TaskEntity` de forma gradual:

- `updatedAt` local.
- `syncState`.
- `deleted` lógico opcional.

Se explicará por qué este diseño permite sincronizar sin perder cambios locales.

### 4) Estados de sincronización y contrato de dominio

Se propondrá un contrato explícito, por ejemplo:

- `SyncState.Pending`
- `SyncState.Synced`
- `SyncState.Failed`

Se justificará cómo este contrato conecta DDD básico con reglas de infraestructura.

### 5) Lectura offline-first en repositorio

Se construirá flujo donde la UI observa Room siempre, y sincronización corre en paralelo controlado.

Se mostrará función principal del repositorio y se explicará línea por línea.

### 6) Escritura local primero y cola de sincronización

Se implementará patrón write-local-first:

1. Guardar en Room con estado pendiente.
2. Programar sync con WorkManager.
3. Actualizar estado al completar sync.

Se explicará por qué mejora UX y resiliencia.

### 7) Orquestador de sincronización

Se introducirá `SyncOrchestrator` como pieza separada de responsabilidad.

Se detallará cómo evita meter demasiada lógica en repositorio.

### 8) Resolución de conflictos simple y gradual

Se enseñará estrategia inicial “last write wins” con advertencia didáctica de límites.

Se explicará en qué escenarios falla y qué evolución se haría en módulos avanzados.

### 9) Exponer estado a UI sin acoplar infraestructura

Se mostrará cómo ViewModel transforma estado técnico en estado de presentación entendible.

Se conectará con UDF y patrón de eventos ya aprendido.

### 10) Errores típicos y diagnóstico guiado

Se cubrirán errores como:

- Duplicación de sync jobs.
- Loop infinito de sincronización.
- Inconsistencia entre timestamp local y remoto.
- UI que no refleja estado real.

Cada error tendrá causa y corrección paso a paso.

### 11) Pruebas del módulo

Se incluirán pruebas unitarias mínimas para:

- Repositorio offline-first.
- Orquestador de sincronización.
- Traducción de estado técnico a UI.

Se explicará por qué esas pruebas son suficientes para este nivel.

### 12) Mini reto final y evidencia de progreso

Se propondrá reto incremental:

Implementar actualización de tarea offline, reiniciar app, recuperar conexión y verificar transición Pending → Synced.

Se pedirá evidencia concreta verificable.

## Código que se planea incluir (sin implementación todavía)

1. `enum class SyncState` o `sealed interface SyncState`.
2. `TaskEntity` ampliada con metadatos de sync.
3. `TasksRepository` con lectura local + trigger de sync.
4. `SyncOrchestrator` con lógica transaccional básica.
5. `WorkManager` request único para sync pendiente.
6. `ViewModel` con estado de sincronización para UI.

## Decisiones de alcance para no adelantar contenido

Este módulo no incluirá:

- CRDTs avanzados.
- Estrategias multi-dispositivo complejas.
- Event sourcing completo.

Solo se cubrirá base midlevel robusta y entendible.

## Criterios de validación antes de dar por cerrado el módulo

1. Narrativa continua sin listas como cuerpo principal de enseñanza.
2. Definición inmediata de términos técnicos nuevos.
3. Código con explicación línea por línea.
4. Conexión explícita con módulos previos.
5. Integración gradual de Clean Architecture + DDD + feature-first.
6. Mini reto final con evidencia verificable.

