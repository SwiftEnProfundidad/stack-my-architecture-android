package com.stackmyarchitecture.fieldops.feature.tasks.di

import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepository
import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepositoryContract
import dagger.Binds
import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
abstract class TasksModule {

    @Binds
    @Singleton
    abstract fun bindTaskRepository(impl: TaskRepository): TaskRepositoryContract
}
