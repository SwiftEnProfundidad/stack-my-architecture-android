package com.stackmyarchitecture.fieldops.navigation

sealed class AppRoute(val route: String) {
    data object Onboarding : AppRoute("onboarding")
    data object Login : AppRoute("login")
    data object Tasks : AppRoute("tasks")
    data object TaskDetail : AppRoute("tasks/{taskId}") {
        fun create(taskId: String): String = "tasks/$taskId"
    }
}
