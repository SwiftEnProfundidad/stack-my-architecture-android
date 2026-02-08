# Nivel Cero · Introducción

Esta es la puerta de entrada de todo el curso. Si hoy te sientes perdido, es normal. No vamos a suponer nada. Vamos a construir desde cero una forma de pensar que después te permitirá crear apps Android reales sin aprender “de memoria”, sino con comprensión de verdad.

Primero vamos a responder una pregunta importante: qué significa programar. Programar significa diseñar instrucciones claras para que un dispositivo haga una tarea. Dicho de otra forma, programar es enseñar a una máquina qué pasos tiene que seguir y en qué orden tiene que seguirlos. Ese detalle del orden es fundamental, porque en programación el orden cambia el resultado.

Imagina una receta de cocina. Si añades ingredientes en un orden incorrecto, el resultado sale mal aunque tengas todos los ingredientes correctos. En programación pasa exactamente lo mismo. Puedes tener buenas ideas, pero si las instrucciones están desordenadas o incompletas, el programa no hará lo que esperas.

Ahora vamos a unir esta idea con tu vida diaria para que no se quede en teoría. Piensa en preparar tu mochila para mañana. Tu cerebro ya ejecuta una secuencia: primero revisas horario, luego eliges cuadernos, después guardas estuche, y al final compruebas agua y cierras la mochila. Eso ya es pensamiento algorítmico. Un algoritmo es precisamente eso: una secuencia de pasos concretos para cumplir un objetivo.

Antes de escribir código real, vamos a hacer una práctica en lenguaje natural. Quiero que describas cómo te prepararías un desayuno sencillo en pasos breves y claros. Evita frases ambiguas como “hacer desayuno”. En su lugar, usa acciones observables como “sacar pan”, “poner leche” o “servir fruta”. Este pequeño cambio de precisión es uno de los hábitos más importantes de un buen desarrollador.

Después de esa práctica, vamos a dar un paso técnico suave con pseudocódigo. El pseudocódigo no es un lenguaje de programación real, pero se parece a una receta lógica y te ayuda a pensar mejor antes de usar sintaxis estricta. Mira este ejemplo y léelo como una historia de decisiones.

```text
INICIO
  mirar hora
  SI es tarde
    desayunar rápido
  SI NO
    desayunar tranquilo
  salir de casa
FIN
```

Vamos a entenderlo línea por línea. La palabra INICIO marca el comienzo del proceso. La línea “mirar hora” recoge información del contexto. Luego aparece una condición con dos caminos posibles. Si es tarde, se elige la opción rápida. Si no es tarde, se elige la opción tranquila. Después del bloque de decisión, se continúa con la acción de salir de casa. FIN marca el cierre del algoritmo.

Si ahora te preguntas para qué sirve hacer esto antes de programar en Kotlin, la respuesta es simple. Sirve para reducir errores. Cuando entiendes cómo se construye una secuencia y cómo se toman decisiones, escribir código se vuelve más natural. Cuando no entiendes esa lógica, el código parece caos.

También quiero anticiparte errores muy típicos del primer día. El primero es escribir pasos demasiado grandes y poco concretos. El segundo es romper el orden lógico. El tercero es olvidar el caso contrario de una decisión, por ejemplo definir qué pasa si la condición no se cumple. El cuarto es usar palabras ambiguas que no se pueden ejecutar de forma clara.

Vamos a cerrar con un mini reto breve pero útil. Diseña un algoritmo para llegar puntual al instituto. Tu algoritmo debe tener al menos ocho pasos y debe incluir al menos una condición con camino alternativo. Cuando termines, compáralo con esta solución de referencia.

```text
INICIO
  sonar alarma
  levantarse
  mirar hora
  SI hora > 07:30
    preparar desayuno rápido
  SI NO
    preparar desayuno normal
  vestirse
  preparar mochila
  salir de casa
  caminar hasta parada
  subir al bus
FIN
```

En esta solución, la condición de la hora ajusta el ritmo de la mañana. Esa adaptación es exactamente lo que hará una app cuando reacciona a estados distintos.

Como evidencia de progreso de esta lección, guarda tres cosas. Guarda tu algoritmo del desayuno, guarda tu algoritmo de puntualidad y escribe una explicación corta con tus palabras sobre por qué el orden importa en programación. Si puedes hacer estas tres cosas con claridad, has comenzado muy bien el curso.
