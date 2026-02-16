package com.stackmyarchitecture.fieldops.feature.tasks.domain

data class Task(
    val id: String,
    val title: String,
    val description: String,
    val status: TaskStatus,
)

enum class TaskStatus { OPEN, IN_PROGRESS, DONE }
