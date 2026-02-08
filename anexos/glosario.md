# Glosario base

## Término 01
- Término: Algoritmo
- Definición muy simple: Lista ordenada de pasos para resolver un problema.
- Ejemplo real: Pasos para preparar la mochila.
- Error común asociado: Poner pasos en desorden.

## Término 02
- Término: Programa
- Definición muy simple: Instrucciones que entiende un dispositivo.
- Ejemplo real: Una app de notas.
- Error común asociado: Pensar que programa y app no son lo mismo.

## Término 03
- Término: Variable
- Definición muy simple: Caja con nombre para guardar un dato.
- Ejemplo real: `edad = 14`.
- Error común asociado: Cambiar el tipo de dato sin control.

## Término 04
- Término: Tipo de dato
- Definición muy simple: La clase de información que guardas.
- Ejemplo real: número, texto, verdadero/falso.
- Error común asociado: Mezclar texto con número sin convertir.

## Término 05
- Término: Condición
- Definición muy simple: Decisión basada en una pregunta.
- Ejemplo real: Si llueve, llevar paraguas.
- Error común asociado: No definir qué pasa en el caso contrario.

## Término 06
- Término: Bucle
- Definición muy simple: Repetir una acción varias veces.
- Ejemplo real: Revisar 10 tareas una por una.
- Error común asociado: Crear un bucle infinito.

## Término 07
- Término: Función
- Definición muy simple: Bloque de pasos con nombre reutilizable.
- Ejemplo real: `calcularTotal()`.
- Error común asociado: Hacer funciones enormes.

## Término 08
- Término: Parámetro
- Definición muy simple: Dato que le pasas a una función.
- Ejemplo real: `saludar(nombre)`.
- Error común asociado: Pasar datos en orden incorrecto.

## Término 09
- Término: Retorno
- Definición muy simple: Resultado que entrega una función.
- Ejemplo real: `sumar(2, 3)` devuelve 5.
- Error común asociado: Olvidar devolver valor cuando hace falta.

## Término 10
- Término: Error de compilación
- Definición muy simple: Fallo que impide construir la app.
- Ejemplo real: Paréntesis sin cerrar.
- Error común asociado: Ignorar el mensaje exacto del compilador.

## Término 11
- Término: Error en ejecución
- Definición muy simple: Fallo que ocurre cuando la app ya está corriendo.
- Ejemplo real: App se cierra al pulsar botón.
- Error común asociado: No revisar el log para encontrar la causa.

## Término 12
- Término: Debug
- Definición muy simple: Buscar y corregir errores.
- Ejemplo real: Revisar valores paso a paso.
- Error común asociado: Cambiar código al azar sin hipótesis.

## Término 13
- Término: IDE
- Definición muy simple: Herramienta para escribir y ejecutar código.
- Ejemplo real: Android Studio.
- Error común asociado: No aprender atajos y paneles básicos.

## Término 14
- Término: Android Studio
- Definición muy simple: IDE oficial para crear apps Android.
- Ejemplo real: Proyecto con Compose.
- Error común asociado: No sincronizar Gradle tras cambios.

## Término 15
- Término: SDK
- Definición muy simple: Paquete de herramientas para desarrollar.
- Ejemplo real: Android SDK 36.
- Error común asociado: No instalar la versión necesaria.

## Término 16
- Término: JDK
- Definición muy simple: Herramientas para compilar código Java/Kotlin.
- Ejemplo real: JDK 17.
- Error común asociado: Usar versión incompatible con AGP.

## Término 17
- Término: Gradle
- Definición muy simple: Sistema que construye la app.
- Ejemplo real: Ejecutar tareas de build.
- Error común asociado: Romper configuración por copiar sin entender.

## Término 18
- Término: AGP
- Definición muy simple: Plugin de Gradle para Android.
- Ejemplo real: AGP 9.0.0.
- Error común asociado: Combinar AGP y Gradle incompatibles.

## Término 19
- Término: Kotlin
- Definición muy simple: Lenguaje principal para Android moderno.
- Ejemplo real: Escribir una pantalla Compose.
- Error común asociado: No entender nullabilidad.

## Término 20
- Término: Null
- Definición muy simple: Valor vacío o inexistente.
- Ejemplo real: `nombre = null`.
- Error común asociado: Forzar valor no nulo y provocar crash.

## Término 21
- Término: Jetpack Compose
- Definición muy simple: Forma moderna de construir interfaz Android.
- Ejemplo real: `Text`, `Button`, `Column`.
- Error común asociado: Mezclar estado sin control.

## Término 22
- Término: Composable
- Definición muy simple: Función que dibuja UI en Compose.
- Ejemplo real: `@Composable fun Pantalla()`.
- Error común asociado: Meter lógica de negocio dentro de UI.

## Término 23
- Término: Estado
- Definición muy simple: Datos actuales que definen lo que ves.
- Ejemplo real: Contador en pantalla.
- Error común asociado: Tener dos fuentes de verdad.

## Término 24
- Término: ViewModel
- Definición muy simple: Clase que guarda estado de pantalla y lógica de UI.
- Ejemplo real: Cargar lista de tareas.
- Error común asociado: Poner llamadas de red directamente en Composable.

## Término 25
- Término: UDF
- Definición muy simple: Flujo de datos en una sola dirección.
- Ejemplo real: Evento -> ViewModel -> nuevo estado -> UI.
- Error común asociado: Modificar estado desde muchos sitios.

## Término 26
- Término: Repositorio
- Definición muy simple: Capa que decide de dónde vienen los datos.
- Ejemplo real: Leer de red o base local.
- Error común asociado: Saltarse el repositorio y acoplar capas.

## Término 27
- Término: Room
- Definición muy simple: Librería para guardar datos en base local.
- Ejemplo real: Guardar tareas sin internet.
- Error común asociado: No definir bien claves y entidades.

## Término 28
- Término: DataStore
- Definición muy simple: Guardado simple para preferencias.
- Ejemplo real: Modo oscuro activado.
- Error común asociado: Usarlo para datos complejos de negocio.

## Término 29
- Término: WorkManager
- Definición muy simple: Ejecuta tareas en segundo plano de forma confiable.
- Ejemplo real: Sincronizar datos más tarde.
- Error común asociado: Usarlo para tareas inmediatas de UI.

## Término 30
- Término: Test
- Definición muy simple: Prueba automática para validar comportamiento.
- Ejemplo real: Comprobar que sumar 2+3 da 5.
- Error común asociado: Escribir pruebas solo al final.

