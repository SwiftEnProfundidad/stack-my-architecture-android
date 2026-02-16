package com.stackmyarchitecture.fieldops.feature.tasks.detail

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepositoryContract
import com.stackmyarchitecture.fieldops.feature.tasks.domain.Task
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

sealed interface TaskDetailUiState {
    data object Loading : TaskDetailUiState
    data class Success(val task: Task) : TaskDetailUiState
    data object NotFound : TaskDetailUiState
}

@HiltViewModel
class TaskDetailViewModel @Inject constructor(
    savedStateHandle: SavedStateHandle,
    private val taskRepository: TaskRepositoryContract,
) : ViewModel() {

    private val taskId: String = checkNotNull(savedStateHandle["taskId"])

    private val _uiState = MutableStateFlow<TaskDetailUiState>(TaskDetailUiState.Loading)
    val uiState: StateFlow<TaskDetailUiState> = _uiState.asStateFlow()

    init {
        viewModelScope.launch {
            val task = taskRepository.getTaskById(taskId)
            _uiState.value = if (task != null) {
                TaskDetailUiState.Success(task)
            } else {
                TaskDetailUiState.NotFound
            }
        }
    }
}
