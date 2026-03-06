# Troubleshooting Android

Este anexo recoge los bloqueos más comunes del track Android y la ruta corta para recuperarte sin romper el hilo de aprendizaje.

## 1. Gradle no sincroniza

**Síntoma**: Android Studio muestra errores de sincronización o dependencias sin resolver.

**Qué revisar**:
- `JDK 17` activo en Gradle JDK.
- Versiones coherentes entre `Gradle`, `AGP` y `Kotlin`.
- Conexión de red si acabas de añadir dependencias nuevas.

**Recuperación mínima**:
1. Abre `gradle/libs.versions.toml` y comprueba versiones base.
2. Ejecuta `./gradlew --version`.
3. Sincroniza de nuevo.
4. Si sigue fallando, limpia caché local solo después de entender el error exacto.

## 2. Compose compila pero la pantalla no refleja cambios

**Síntoma**: pulsas botones o cambias estado y la UI no se actualiza como esperas.

**Qué revisar**:
- Que el estado tenga una única fuente de verdad.
- Que el `ViewModel` emita nuevo estado en vez de mutar estructuras invisibles para la UI.
- Que no estés guardando lógica de negocio dentro del composable.

**Recuperación mínima**:
1. Revisa el flujo `evento -> ViewModel -> nuevo estado -> UI`.
2. Añade log temporal o test pequeño para verificar la transición.
3. Reduce la pantalla a un caso mínimo reproducible.

## 3. Room rompe al cambiar esquema

**Síntoma**: la app crashea tras cambiar entidad o versión de base de datos.

**Qué revisar**:
- Si aumentaste `version` en `@Database`.
- Si existe migración o estrategia explícita para desarrollo.
- Si el cambio afecta datos ya persistidos.

**Recuperación mínima**:
1. Identifica qué cambió en la entidad.
2. Decide si necesitas migración real o recreación controlada para entorno de curso.
3. Ejecuta tests de persistencia antes de seguir.

## 4. WorkManager no ejecuta cuando esperabas

**Síntoma**: una tarea programada no corre o tarda más de lo esperado.

**Qué revisar**:
- `constraints` demasiado restrictivos.
- Confusión entre trabajo inmediato y trabajo persistente diferido.
- Estado real del dispositivo o emulador.

**Recuperación mínima**:
1. Revisa por qué usaste `WorkManager` y no coroutine directa.
2. Simplifica constraints.
3. Verifica logs y estado del worker.

## 5. Offline-first parece funcionar pero sync falla

**Síntoma**: la app guarda localmente pero no reconcilia bien al volver la red.

**Qué revisar**:
- Estados `PENDING`, `SYNCED`, `ERROR`.
- Payload real enviado al backend.
- Estrategia de conflictos y reintentos.

**Recuperación mínima**:
1. Reproduce con una sola entidad.
2. Añade observabilidad con `operationId`.
3. Ejecuta el test de integración de sync antes de tocar producción.

## 6. La prueba falla de forma aleatoria

**Síntoma**: test verde y rojo sin cambios aparentes.

**Qué revisar**:
- Dependencia de tiempo real.
- Estado compartido entre tests.
- Esperas no deterministas.

**Recuperación mínima**:
1. Inyecta reloj o dispatcher de test.
2. Aísla fixtures.
3. Haz el caso mínimo.

## Regla de oro

Si te bloqueas, vuelve al último punto con evidencia verde y reduce el problema a una sola capa. En Android, depurar dos capas a la vez casi siempre multiplica ruido.
