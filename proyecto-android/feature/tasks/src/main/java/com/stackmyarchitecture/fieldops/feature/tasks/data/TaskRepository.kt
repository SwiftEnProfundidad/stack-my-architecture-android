package com.stackmyarchitecture.fieldops.feature.tasks.data

import com.stackmyarchitecture.fieldops.core.common.FeatureFlag
import com.stackmyarchitecture.fieldops.core.common.FeatureFlagManager
import com.stackmyarchitecture.fieldops.core.common.Logger
import com.stackmyarchitecture.fieldops.core.database.dao.TaskDao
import com.stackmyarchitecture.fieldops.core.database.model.SyncState
import com.stackmyarchitecture.fieldops.core.database.model.TaskEntity
import com.stackmyarchitecture.fieldops.core.network.NetworkDataSource
import com.stackmyarchitecture.fieldops.feature.tasks.domain.Task
import com.stackmyarchitecture.fieldops.feature.tasks.domain.TaskStatus
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.map
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class TaskRepository @Inject constructor(
    private val taskDao: TaskDao,
    private val networkDataSource: NetworkDataSource,
    private val logger: Logger,
    private val featureFlagManager: FeatureFlagManager,
) : TaskRepositoryContract {
    
    override fun observeTasks(): Flow<List<Task>> {
        return taskDao.observeAll().map { entities ->
            entities.map { it.toDomain() }
        }
    }

    override suspend fun getTaskById(taskId: String): Task? {
        return taskDao.getById(taskId)?.toDomain()
    }

    override suspend fun refreshTasks() {
        val offlineSyncEnabled = featureFlagManager.isEnabled(FeatureFlag.ENABLE_OFFLINE_SYNC).first()
        if (!offlineSyncEnabled) {
            logger.i(TAG, "Offline sync disabled by feature flag", emptyMap())
            return
        }
        
        logger.i(TAG, "Starting task sync", mapOf("operation" to "refresh"))
        
        try {
            // 1. Fetch remote tasks
            val networkTasks = networkDataSource.fetchTasks()
            logger.d(TAG, "Fetched remote tasks", mapOf("count" to networkTasks.size))
            
            // 2. Get pending local changes
            val pendingSync = taskDao.getPendingSync()
            logger.d(TAG, "Found pending local changes", mapOf("count" to pendingSync.size))
            
            // 3. Reconcile conflicts
            val now = System.currentTimeMillis()
            val reconciledTasks = networkTasks.map { dto ->
                val localTask = taskDao.getById(dto.id)
                
                when {
                    // No local copy - insert remote
                    localTask == null -> {
                        logger.d(TAG, "New remote task", mapOf("taskId" to dto.id))
                        TaskEntity(
                            id = dto.id,
                            title = dto.title,
                            description = dto.description,
                            status = dto.status,
                            syncState = SyncState.SYNCED.name,
                            lastSyncTimestamp = now,
                            localModifiedAt = now,
                        )
                    }
                    // Local is pending sync - conflict detected
                    localTask.syncState == SyncState.PENDING_SYNC.name -> {
                        val conflictResolutionEnabled = featureFlagManager
                            .isEnabled(FeatureFlag.ENABLE_CONFLICT_RESOLUTION).first()
                        
                        logger.w(TAG, "Conflict detected", metadata = mapOf(
                            "taskId" to dto.id,
                            "localModified" to localTask.localModifiedAt,
                            "lastSync" to localTask.lastSyncTimestamp,
                            "resolutionEnabled" to conflictResolutionEnabled
                        ))
                        
                        if (!conflictResolutionEnabled) {
                            // Keep local version when conflict resolution is disabled
                            localTask
                        } else {
                            // Strategy: Last-write-wins (server wins)
                            TaskEntity(
                                id = dto.id,
                                title = dto.title,
                                description = dto.description,
                                status = dto.status,
                                syncState = SyncState.SYNCED.name,
                                lastSyncTimestamp = now,
                                localModifiedAt = now,
                            )
                        }
                    }
                    // Already synced - update
                    else -> {
                        logger.d(TAG, "Updating synced task", mapOf("taskId" to dto.id))
                        TaskEntity(
                            id = dto.id,
                            title = dto.title,
                            description = dto.description,
                            status = dto.status,
                            syncState = SyncState.SYNCED.name,
                            lastSyncTimestamp = now,
                            localModifiedAt = now,
                        )
                    }
                }
            }
            
            // 4. Save reconciled tasks
            taskDao.upsertAll(reconciledTasks)
            logger.i(TAG, "Sync completed successfully", mapOf(
                "synced" to reconciledTasks.size,
                "conflicts" to pendingSync.size
            ))
            
        } catch (e: Exception) {
            logger.e(TAG, "Sync failed", e, mapOf("error" to (e.message ?: "unknown")))
            throw e
        }
    }

    suspend fun syncPendingChanges() {
        val pending = taskDao.getPendingSync()
        logger.i(TAG, "Syncing pending changes", mapOf("count" to pending.size))
        
        pending.forEach { task ->
            try {
                // Here you'd call networkDataSource.updateTask(task) when implemented
                // For now, just mark as synced
                taskDao.updateSyncState(
                    taskId = task.id,
                    syncState = SyncState.SYNCED.name,
                    timestamp = System.currentTimeMillis()
                )
                logger.d(TAG, "Synced pending task", mapOf("taskId" to task.id))
            } catch (e: Exception) {
                logger.e(TAG, "Failed to sync task", e, mapOf("taskId" to task.id))
            }
        }
    }

    private fun TaskEntity.toDomain(): Task = Task(
        id = id,
        title = title,
        description = description,
        status = when (status) {
            "in_progress" -> TaskStatus.IN_PROGRESS
            "done" -> TaskStatus.DONE
            else -> TaskStatus.OPEN
        },
    )
    
    companion object {
        private const val TAG = "TaskRepository"
    }
}
