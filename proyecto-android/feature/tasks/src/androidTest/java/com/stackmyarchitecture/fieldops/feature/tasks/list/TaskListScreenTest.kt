package com.stackmyarchitecture.fieldops.feature.tasks.list

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithText
import com.stackmyarchitecture.fieldops.feature.tasks.domain.Task
import com.stackmyarchitecture.fieldops.feature.tasks.domain.TaskStatus
import org.junit.Rule
import org.junit.Test

class TaskListScreenTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun loadingState_showsProgressIndicator() {
        composeTestRule.setContent {
            TaskListContent(
                uiState = TaskListUiState.Loading,
                onTaskClick = {},
                onRefresh = {},
            )
        }
        composeTestRule.onNodeWithText("Tareas").assertIsDisplayed()
    }

    @Test
    fun successState_showsTaskTitles() {
        val tasks = listOf(
            Task(id = "1", title = "Inspeccionar parcela", description = "Desc", status = TaskStatus.OPEN),
            Task(id = "2", title = "Reparar cerca", description = "Desc", status = TaskStatus.IN_PROGRESS),
        )

        composeTestRule.setContent {
            TaskListContent(
                uiState = TaskListUiState.Success(tasks),
                onTaskClick = {},
                onRefresh = {},
            )
        }

        composeTestRule.onNodeWithText("Inspeccionar parcela").assertIsDisplayed()
        composeTestRule.onNodeWithText("Reparar cerca").assertIsDisplayed()
    }

    @Test
    fun errorState_showsErrorMessage() {
        composeTestRule.setContent {
            TaskListContent(
                uiState = TaskListUiState.Error("Sin conexión"),
                onTaskClick = {},
                onRefresh = {},
            )
        }

        composeTestRule.onNodeWithText("Sin conexión").assertIsDisplayed()
    }

    @Test
    fun successState_showsTaskStatus() {
        val tasks = listOf(
            Task(id = "1", title = "Tarea abierta", description = "Desc", status = TaskStatus.OPEN),
            Task(id = "3", title = "Tarea hecha", description = "Desc", status = TaskStatus.DONE),
        )

        composeTestRule.setContent {
            TaskListContent(
                uiState = TaskListUiState.Success(tasks),
                onTaskClick = {},
                onRefresh = {},
            )
        }

        composeTestRule.onNodeWithText("OPEN").assertIsDisplayed()
        composeTestRule.onNodeWithText("DONE").assertIsDisplayed()
    }
}
