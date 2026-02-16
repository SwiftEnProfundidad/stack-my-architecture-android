package com.stackmyarchitecture.fieldops.core.common

import com.google.common.truth.Truth.assertThat
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.test.runTest
import org.junit.Before
import org.junit.Test

class FeatureFlagManagerTest {

    private lateinit var manager: FeatureFlagManager
    private lateinit var fakeDataStore: FakeFeatureFlagDataStore
    private lateinit var fakeLogger: FakeLogger

    @Before
    fun setup() {
        fakeDataStore = FakeFeatureFlagDataStore()
        fakeLogger = FakeLogger()
        manager = TestableFeatureFlagManager(fakeDataStore, fakeLogger)
    }

    @Test
    fun `isEnabled returns default value when flag not set`() = runTest {
        val enabled = manager.isEnabled(FeatureFlag.ENABLE_OFFLINE_SYNC).first()
        assertThat(enabled).isTrue()
    }

    @Test
    fun `isEnabled returns stored value when flag is set`() = runTest {
        manager.setEnabled(FeatureFlag.ENABLE_OFFLINE_SYNC, false)
        val enabled = manager.isEnabled(FeatureFlag.ENABLE_OFFLINE_SYNC).first()
        assertThat(enabled).isFalse()
    }

    @Test
    fun `setEnabled logs flag change`() = runTest {
        manager.setEnabled(FeatureFlag.ENABLE_BACKGROUND_SYNC, false)
        
        assertThat(fakeLogger.infos).hasSize(1)
        assertThat(fakeLogger.infos[0]).contains("Feature flag changed")
        assertThat(fakeLogger.infos[0]).contains("enable_background_sync")
    }

    @Test
    fun `reset removes flag and returns to default`() = runTest {
        manager.setEnabled(FeatureFlag.ENABLE_CONFLICT_RESOLUTION, false)
        assertThat(manager.isEnabled(FeatureFlag.ENABLE_CONFLICT_RESOLUTION).first()).isFalse()
        
        manager.reset(FeatureFlag.ENABLE_CONFLICT_RESOLUTION)
        assertThat(manager.isEnabled(FeatureFlag.ENABLE_CONFLICT_RESOLUTION).first()).isTrue()
    }

    @Test
    fun `resetAll clears all flags`() = runTest {
        manager.setEnabled(FeatureFlag.ENABLE_OFFLINE_SYNC, false)
        manager.setEnabled(FeatureFlag.ENABLE_BACKGROUND_SYNC, false)
        
        manager.resetAll()
        
        assertThat(manager.isEnabled(FeatureFlag.ENABLE_OFFLINE_SYNC).first()).isTrue()
        assertThat(manager.isEnabled(FeatureFlag.ENABLE_BACKGROUND_SYNC).first()).isTrue()
    }
}

private class TestableFeatureFlagManager(
    private val dataStore: FakeFeatureFlagDataStore,
    private val logger: Logger,
) : FeatureFlagManager {

    override fun isEnabled(flag: FeatureFlag): Flow<Boolean> {
        return dataStore.getFlag(flag.key).map { value ->
            value ?: flag.defaultValue
        }
    }

    override suspend fun setEnabled(flag: FeatureFlag, enabled: Boolean) {
        logger.i("FeatureFlagManager", "Feature flag changed", mapOf(
            "flag" to flag.key,
            "enabled" to enabled,
            "previous" to flag.defaultValue
        ))
        dataStore.setFlag(flag.key, enabled)
    }

    override suspend fun reset(flag: FeatureFlag) {
        logger.i("FeatureFlagManager", "Feature flag reset", mapOf("flag" to flag.key))
        dataStore.removeFlag(flag.key)
    }

    override suspend fun resetAll() {
        logger.i("FeatureFlagManager", "All feature flags reset", emptyMap())
        dataStore.clear()
    }
}

private class FakeFeatureFlagDataStore {
    private val flags = mutableMapOf<String, MutableStateFlow<Boolean?>>()

    fun getFlag(key: String): Flow<Boolean?> {
        return flags.getOrPut(key) { MutableStateFlow(null) }
    }

    suspend fun setFlag(key: String, value: Boolean) {
        flags.getOrPut(key) { MutableStateFlow(null) }.value = value
    }

    suspend fun removeFlag(key: String) {
        flags[key]?.value = null
    }

    suspend fun clear() {
        flags.values.forEach { it.value = null }
    }
}

private class FakeLogger : Logger {
    val infos = mutableListOf<String>()
    
    override fun d(tag: String, message: String, metadata: Map<String, Any>) {}
    override fun i(tag: String, message: String, metadata: Map<String, Any>) {
        infos.add("$tag: $message | $metadata")
    }
    override fun w(tag: String, message: String, throwable: Throwable?, metadata: Map<String, Any>) {}
    override fun e(tag: String, message: String, throwable: Throwable?, metadata: Map<String, Any>) {}
}
