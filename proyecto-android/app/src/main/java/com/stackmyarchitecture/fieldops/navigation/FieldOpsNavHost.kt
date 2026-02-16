package com.stackmyarchitecture.fieldops.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.stackmyarchitecture.fieldops.feature.auth.LoginScreen
import com.stackmyarchitecture.fieldops.feature.onboarding.OnboardingScreen
import com.stackmyarchitecture.fieldops.feature.tasks.list.TaskListScreen
import com.stackmyarchitecture.fieldops.feature.tasks.detail.TaskDetailScreen

@Composable
fun FieldOpsNavHost() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = AppRoute.Onboarding.route) {
        composable(AppRoute.Onboarding.route) {
            OnboardingScreen(
                onContinue = {
                    navController.navigate(AppRoute.Login.route) {
                        popUpTo(AppRoute.Onboarding.route) { inclusive = true }
                    }
                }
            )
        }
        composable(AppRoute.Login.route) {
            LoginScreen(
                onLoginSuccess = {
                    navController.navigate(AppRoute.Tasks.route) {
                        popUpTo(AppRoute.Login.route) { inclusive = true }
                    }
                }
            )
        }
        composable(AppRoute.Tasks.route) {
            TaskListScreen(
                onTaskClick = { taskId ->
                    navController.navigate(AppRoute.TaskDetail.create(taskId))
                }
            )
        }
        composable(
            route = AppRoute.TaskDetail.route,
            arguments = listOf(navArgument("taskId") { type = NavType.StringType })
        ) { backStackEntry ->
            val taskId = backStackEntry.arguments?.getString("taskId") ?: return@composable
            TaskDetailScreen(
                taskId = taskId,
                onBack = { navController.popBackStack() }
            )
        }
    }
}
