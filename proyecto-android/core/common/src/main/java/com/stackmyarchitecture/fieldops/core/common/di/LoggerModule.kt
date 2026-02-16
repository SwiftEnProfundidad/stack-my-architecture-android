package com.stackmyarchitecture.fieldops.core.common.di

import com.stackmyarchitecture.fieldops.core.common.FeatureFlagDataStore
import com.stackmyarchitecture.fieldops.core.common.FeatureFlagManager
import com.stackmyarchitecture.fieldops.core.common.FeatureFlagManagerImpl
import com.stackmyarchitecture.fieldops.core.common.Logger
import com.stackmyarchitecture.fieldops.core.common.StructuredLogger
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object LoggerModule {

    @Provides
    @Singleton
    fun provideLogger(): Logger = StructuredLogger()

    @Provides
    @Singleton
    fun provideFeatureFlagManager(
        dataStore: FeatureFlagDataStore,
        logger: Logger,
    ): FeatureFlagManager = FeatureFlagManagerImpl(dataStore, logger)
}
