package com.stackmyarchitecture.fieldops.feature.tasks.data

import com.stackmyarchitecture.fieldops.feature.tasks.domain.Task
import kotlinx.coroutines.flow.Flow

interface TaskRepositoryContract {
    fun observeTasks(): Flow<List<Task>>
    suspend fun getTaskById(taskId: String): Task?
    suspend fun refreshTasks()
}
