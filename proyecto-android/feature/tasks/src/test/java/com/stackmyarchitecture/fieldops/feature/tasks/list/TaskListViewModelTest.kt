package com.stackmyarchitecture.fieldops.feature.tasks.list

import com.stackmyarchitecture.fieldops.core.testing.MainDispatcherRule
import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepositoryContract
import com.stackmyarchitecture.fieldops.feature.tasks.domain.Task
import com.stackmyarchitecture.fieldops.feature.tasks.domain.TaskStatus
import com.google.common.truth.Truth.assertThat
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import app.cash.turbine.test
import kotlinx.coroutines.test.runTest
import org.junit.Rule
import org.junit.Test

class TaskListViewModelTest {

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    @Test
    fun `initial state is loading`() {
        val repo = FakeTaskRepository()
        val viewModel = TaskListViewModel(repo)
        assertThat(viewModel.uiState.value).isInstanceOf(TaskListUiState.Loading::class.java)
    }

    @Test
    fun `emitting tasks transitions to success`() = runTest {
        val repo = FakeTaskRepository()
        val viewModel = TaskListViewModel(repo)
        val tasks = listOf(
            Task("1", "Tarea 1", "Desc", TaskStatus.OPEN),
            Task("2", "Tarea 2", "Desc", TaskStatus.DONE),
        )
        repo.emitTasks(tasks)

        viewModel.uiState.test {
            val state = expectMostRecentItem()
            assertThat(state).isInstanceOf(TaskListUiState.Success::class.java)
            assertThat((state as TaskListUiState.Success).tasks).hasSize(2)
        }
    }

    @Test
    fun `refresh calls repository`() = runTest {
        val repo = FakeTaskRepository()
        val viewModel = TaskListViewModel(repo)
        viewModel.refresh()
        assertThat(repo.refreshCount).isGreaterThan(0)
    }
}

private class FakeTaskRepository : TaskRepositoryContract {
    private val _tasks = MutableStateFlow<List<Task>>(emptyList())
    var refreshCount = 0
        private set

    override fun observeTasks(): Flow<List<Task>> = _tasks

    override suspend fun refreshTasks() { refreshCount++ }

    override suspend fun getTaskById(taskId: String): Task? {
        return _tasks.value.firstOrNull { it.id == taskId }
    }

    fun emitTasks(tasks: List<Task>) { _tasks.value = tasks }
}
