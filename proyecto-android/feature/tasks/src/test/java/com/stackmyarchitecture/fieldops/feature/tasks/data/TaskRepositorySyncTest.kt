package com.stackmyarchitecture.fieldops.feature.tasks.data

import com.google.common.truth.Truth.assertThat
import com.stackmyarchitecture.fieldops.core.common.FeatureFlag
import com.stackmyarchitecture.fieldops.core.common.FeatureFlagManager
import com.stackmyarchitecture.fieldops.core.common.Logger
import com.stackmyarchitecture.fieldops.core.database.dao.TaskDao
import com.stackmyarchitecture.fieldops.core.database.model.SyncState
import com.stackmyarchitecture.fieldops.core.database.model.TaskEntity
import com.stackmyarchitecture.fieldops.core.network.NetworkDataSource
import com.stackmyarchitecture.fieldops.core.network.model.NetworkTaskDto
import com.stackmyarchitecture.fieldops.core.testing.MainDispatcherRule
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flowOf
import kotlinx.coroutines.test.runTest
import org.junit.Before
import org.junit.Rule
import org.junit.Test

class TaskRepositorySyncTest {

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    private lateinit var repository: TaskRepository
    private lateinit var fakeDao: FakeTaskDao
    private lateinit var fakeNetwork: FakeNetworkDataSource
    private lateinit var fakeLogger: FakeLogger
    private lateinit var fakeFeatureFlags: FakeFeatureFlagManager

    @Before
    fun setup() {
        fakeDao = FakeTaskDao()
        fakeNetwork = FakeNetworkDataSource()
        fakeLogger = FakeLogger()
        fakeFeatureFlags = FakeFeatureFlagManager()
        repository = TaskRepository(fakeDao, fakeNetwork, fakeLogger, fakeFeatureFlags)
    }

    @Test
    fun `refreshTasks with no local data inserts remote tasks`() = runTest {
        fakeNetwork.tasks = listOf(
            NetworkTaskDto("1", "Task 1", "Desc 1", "open"),
            NetworkTaskDto("2", "Task 2", "Desc 2", "done"),
        )

        repository.refreshTasks()

        assertThat(fakeDao.tasks).hasSize(2)
        assertThat(fakeDao.tasks[0].id).isEqualTo("1")
        assertThat(fakeDao.tasks[0].syncState).isEqualTo(SyncState.SYNCED.name)
        assertThat(fakeDao.tasks[1].id).isEqualTo("2")
    }

    @Test
    fun `refreshTasks with pending local changes detects conflict`() = runTest {
        // Local task pending sync
        fakeDao.tasks.add(
            TaskEntity(
                id = "1",
                title = "Local Title",
                description = "Local Desc",
                status = "in_progress",
                syncState = SyncState.PENDING_SYNC.name,
                lastSyncTimestamp = 1000L,
                localModifiedAt = 2000L,
            )
        )

        // Remote task with different data
        fakeNetwork.tasks = listOf(
            NetworkTaskDto("1", "Remote Title", "Remote Desc", "done"),
        )

        repository.refreshTasks()

        // Server wins (last-write-wins strategy)
        assertThat(fakeDao.tasks).hasSize(1)
        assertThat(fakeDao.tasks[0].title).isEqualTo("Remote Title")
        assertThat(fakeDao.tasks[0].syncState).isEqualTo(SyncState.SYNCED.name)
        
        // Verify conflict was logged
        assertThat(fakeLogger.warnings).isNotEmpty()
        assertThat(fakeLogger.warnings[0]).contains("Conflict detected")
    }

    @Test
    fun `syncPendingChanges marks tasks as synced`() = runTest {
        fakeDao.tasks.add(
            TaskEntity(
                id = "1",
                title = "Pending Task",
                description = "Desc",
                status = "open",
                syncState = SyncState.PENDING_SYNC.name,
            )
        )

        repository.syncPendingChanges()

        assertThat(fakeDao.syncStateUpdates).hasSize(1)
        assertThat(fakeDao.syncStateUpdates[0].first).isEqualTo("1")
        assertThat(fakeDao.syncStateUpdates[0].second).isEqualTo(SyncState.SYNCED.name)
    }
}

private class FakeTaskDao : TaskDao {
    val tasks = mutableListOf<TaskEntity>()
    val syncStateUpdates = mutableListOf<Triple<String, String, Long>>()

    override fun observeAll() = throw NotImplementedError()
    override suspend fun getById(taskId: String) = tasks.find { it.id == taskId }
    override suspend fun getPendingSync() = tasks.filter { it.syncState == SyncState.PENDING_SYNC.name }
    override suspend fun getConflicts() = tasks.filter { it.syncState == SyncState.CONFLICT.name }
    override suspend fun upsertAll(tasks: List<TaskEntity>) {
        this.tasks.clear()
        this.tasks.addAll(tasks)
    }
    override suspend fun upsert(task: TaskEntity) { tasks.add(task) }
    override suspend fun updateSyncState(taskId: String, syncState: String, timestamp: Long) {
        syncStateUpdates.add(Triple(taskId, syncState, timestamp))
        tasks.find { it.id == taskId }?.let { task ->
            val index = tasks.indexOf(task)
            tasks[index] = task.copy(syncState = syncState, lastSyncTimestamp = timestamp)
        }
    }
    override suspend fun deleteAll() { tasks.clear() }
}

private class FakeNetworkDataSource : NetworkDataSource {
    var tasks = emptyList<NetworkTaskDto>()
    override suspend fun fetchTasks() = tasks
    override fun authenticate(email: String, password: String) = true
}

private class FakeLogger : Logger {
    val debugs = mutableListOf<String>()
    val infos = mutableListOf<String>()
    val warnings = mutableListOf<String>()
    val errors = mutableListOf<String>()

    override fun d(tag: String, message: String, metadata: Map<String, Any>) {
        debugs.add("$tag: $message | $metadata")
    }
    override fun i(tag: String, message: String, metadata: Map<String, Any>) {
        infos.add("$tag: $message | $metadata")
    }
    override fun w(tag: String, message: String, throwable: Throwable?, metadata: Map<String, Any>) {
        warnings.add("$tag: $message | $metadata")
    }
    override fun e(tag: String, message: String, throwable: Throwable?, metadata: Map<String, Any>) {
        errors.add("$tag: $message | $metadata")
    }
}

private class FakeFeatureFlagManager : FeatureFlagManager {
    private val flags = mutableMapOf<String, Boolean>()
    
    override fun isEnabled(flag: FeatureFlag): Flow<Boolean> {
        return flowOf(flags[flag.key] ?: flag.defaultValue)
    }
    
    override suspend fun setEnabled(flag: FeatureFlag, enabled: Boolean) {
        flags[flag.key] = enabled
    }
    
    override suspend fun reset(flag: FeatureFlag) {
        flags.remove(flag.key)
    }
    
    override suspend fun resetAll() {
        flags.clear()
    }
}
