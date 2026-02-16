package com.stackmyarchitecture.fieldops.feature.tasks.list

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepositoryContract
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class TaskListViewModel @Inject constructor(
    private val taskRepository: TaskRepositoryContract,
) : ViewModel() {

    val uiState: StateFlow<TaskListUiState> = taskRepository.observeTasks()
        .map<_, TaskListUiState> { tasks -> TaskListUiState.Success(tasks) }
        .catch { emit(TaskListUiState.Error(it.message ?: "Error desconocido")) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), TaskListUiState.Loading)

    init {
        refresh()
    }

    fun refresh() {
        viewModelScope.launch {
            try {
                taskRepository.refreshTasks()
            } catch (e: Exception) {
                // Error al refrescar; la UI mostrará datos del cache o estado error
            }
        }
    }
}
