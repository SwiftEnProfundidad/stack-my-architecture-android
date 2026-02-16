package com.stackmyarchitecture.rutinadiaria.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.stackmyarchitecture.rutinadiaria.screens.InicioScreen
import com.stackmyarchitecture.rutinadiaria.screens.ResumenScreen
import com.stackmyarchitecture.rutinadiaria.screens.RutinaScreen

@Composable
fun AppNavigation() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "inicio") {
        composable("inicio") {
            InicioScreen(
                onComenzar = { navController.navigate("rutina") }
            )
        }
        composable("rutina") {
            RutinaScreen(
                onRutinaValida = { nombreRutina ->
                    navController.navigate("resumen/$nombreRutina")
                }
            )
        }
        composable("resumen/{nombre}") { backStackEntry ->
            val nombre = backStackEntry.arguments?.getString("nombre") ?: ""
            ResumenScreen(
                nombreRutina = nombre,
                onVolver = {
                    navController.popBackStack("inicio", inclusive = false)
                }
            )
        }
    }
}
