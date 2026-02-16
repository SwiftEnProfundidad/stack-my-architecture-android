package com.stackmyarchitecture.fieldops.core.datastore.di

import com.stackmyarchitecture.fieldops.core.datastore.UserPreferences
import com.stackmyarchitecture.fieldops.core.datastore.UserPreferencesDataStore
import dagger.Binds
import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
abstract class DataStoreModule {

    @Binds
    @Singleton
    abstract fun bindUserPreferences(impl: UserPreferencesDataStore): UserPreferences
}
