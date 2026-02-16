# Proyecto Nivel Cero: Rutina Diaria

Mini app Compose que integra todo lo aprendido en Nivel Cero:
- Variables y tipos
- Condicionales
- Funciones
- Compose básico (Column, Text, Button, TextField)
- Validación de inputs
- Navegación simple entre 3 pantallas

## Estructura

```
app/src/main/java/.../
  MainActivity.kt          — Punto de entrada
  navigation/
    AppNavigation.kt       — NavHost con 3 rutas
  screens/
    InicioScreen.kt        — Pantalla de bienvenida
    RutinaScreen.kt        — Captura y validación de rutina
    ResumenScreen.kt       — Resumen final
```

## Cómo ejecutar

1. Abre este proyecto en Android Studio
2. Sincroniza Gradle
3. Ejecuta en emulador o dispositivo

## Evidencia esperada

- Captura de las 3 pantallas funcionando
- Texto explicando qué hace cada pantalla
- Descripción de la validación implementada
