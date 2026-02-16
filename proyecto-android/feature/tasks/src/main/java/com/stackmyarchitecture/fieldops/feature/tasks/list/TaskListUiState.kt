package com.stackmyarchitecture.fieldops.feature.tasks.list

import com.stackmyarchitecture.fieldops.feature.tasks.domain.Task

sealed interface TaskListUiState {
    data object Loading : TaskListUiState
    data class Success(val tasks: List<Task>) : TaskListUiState
    data class Error(val message: String) : TaskListUiState
}
