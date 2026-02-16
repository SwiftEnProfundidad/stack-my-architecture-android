package com.stackmyarchitecture.fieldops.core.common

import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

interface FeatureFlagManager {
    fun isEnabled(flag: FeatureFlag): Flow<Boolean>
    suspend fun setEnabled(flag: FeatureFlag, enabled: Boolean)
    suspend fun reset(flag: FeatureFlag)
    suspend fun resetAll()
}

class FeatureFlagManagerImpl(
    private val dataStore: FeatureFlagDataStore,
    private val logger: Logger,
) : FeatureFlagManager {

    override fun isEnabled(flag: FeatureFlag): Flow<Boolean> {
        return dataStore.getFlag(flag.key).map { value ->
            value ?: flag.defaultValue
        }
    }

    override suspend fun setEnabled(flag: FeatureFlag, enabled: Boolean) {
        logger.i(TAG, "Feature flag changed", mapOf(
            "flag" to flag.key,
            "enabled" to enabled,
            "previous" to flag.defaultValue
        ))
        dataStore.setFlag(flag.key, enabled)
    }

    override suspend fun reset(flag: FeatureFlag) {
        logger.i(TAG, "Feature flag reset", mapOf("flag" to flag.key))
        dataStore.removeFlag(flag.key)
    }

    override suspend fun resetAll() {
        logger.i(TAG, "All feature flags reset", emptyMap())
        dataStore.clear()
    }

    companion object {
        private const val TAG = "FeatureFlagManager"
    }
}
