# Preguntas de entrevista Android con respuestas de criterio

Este anexo no está pensado para memorizar frases. Está pensado para entrenar cómo razonar en voz alta cuando alguien te pregunta por decisiones técnicas de tu proyecto. En una entrevista real, lo que más valoran no es que repitas definiciones perfectas, sino que puedas conectar contexto, riesgo y decisión de forma clara.

Una pregunta muy común es por qué elegiste una arquitectura en capas con ViewModel, repositorios y casos de uso. Una respuesta fuerte no dice solo “porque es lo recomendado”. Una respuesta fuerte explica que necesitabas separar comportamiento de negocio de infraestructura para poder cambiar persistencia o red sin romper la lógica principal del producto. También explica que ese diseño reduce el coste de pruebas porque cada capa puede validarse con foco.

Otra pregunta habitual es cómo manejaste estado de UI en Compose cuando hay carga de datos, errores y reintentos. Aquí conviene explicar que modelaste estado explícito para evitar comportamientos implícitos difíciles de depurar. Cuando `isLoading`, `items` y `message` viven en un estado coherente, la pantalla deja de depender de efectos laterales. Eso mejora predictibilidad y reduce bugs intermitentes.

```kotlin
package com.stackmyarchitecture.interview

data class ScreenState(
    val isLoading: Boolean = false,
    val content: List<String> = emptyList(),
    val errorMessage: String? = null
)
```

Si te preguntan por qué incluiste Room y DataStore en lugar de depender solo de red, la clave está en experiencia de usuario y resiliencia. Room te da continuidad de datos cuando la conectividad falla o fluctúa. DataStore te permite persistir configuración ligera sin fricción. Juntas, estas dos piezas evitan que la app se sienta frágil cuando el entorno no es ideal.

En entrevistas de nivel junior avanzado o semisenior también suele aparecer la pregunta sobre inyección de dependencias con Hilt. Lo más convincente aquí es explicar que la DI no es para “hacer código más bonito”, sino para controlar composición del sistema y facilitar pruebas. Cuando cada componente recibe dependencias por contrato, puedes sustituir implementaciones en test sin hacks ni estado global oculto.

```kotlin
package com.stackmyarchitecture.interview

interface TasksRepository {
    suspend fun refresh()
}

class RefreshTasksUseCase(
    private val repository: TasksRepository
) {
    suspend fun execute() {
        repository.refresh()
    }
}
```

Cuando salga el tema de rendimiento, evita caer en respuestas genéricas. En lugar de decir “optimicé la app”, cuenta qué mediste y qué decisión tomaste con esa medición. Por ejemplo, que usaste Macrobenchmark para observar startup p95 y que al detectar degradación moviste inicializaciones no críticas fuera del arranque principal. Esa conexión entre señal y acción es exactamente lo que busca un entrevistador técnico.

Con seguridad pasa algo parecido. Si te preguntan cómo protegiste datos sensibles, no basta con mencionar “usé buenas prácticas”. Lo útil es explicar que separaste secretos del código, usaste variables de entorno para firma y evitaste persistir datos críticos en almacenamiento inadecuado. Si además puedes decir qué riesgo evitaste con cada decisión, la respuesta gana mucha fuerza.

También es frecuente que pidan un ejemplo de trade-off real. Esta pregunta no busca una solución perfecta, busca madurez. Puedes contar que mantuviste dos versiones de contrato temporalmente para evitar bloqueo entre equipos, aceptando complejidad transitoria y retirándola con criterios de adopción y estabilidad. Esa historia muestra que sabes equilibrar entrega y salud técnica, no solo elegir “lo más puro”.

Si aparece la pregunta de cómo te organizas cuando hay incidentes en producción, la mejor respuesta combina calma y método. Primero contener impacto con rollback o freeze de rollout, luego observar señales para delimitar alcance, después corregir y finalmente documentar aprendizaje para evitar recurrencia. Cuando lo explicas así, transmites que puedes operar bajo presión sin improvisar de forma peligrosa.

Este anexo te deja una idea final que vale oro para entrevistas y para trabajo real. Tu nivel no lo define cuántas tecnologías conoces de memoria. Tu nivel lo define cómo decides cuando hay incertidumbre y cómo explicas esas decisiones con evidencia y sentido de producto.
