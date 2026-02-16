package com.stackmyarchitecture.fieldops.feature.tasks.sync

import android.content.Context
import androidx.hilt.work.HiltWorker
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import com.stackmyarchitecture.fieldops.core.common.FeatureFlag
import com.stackmyarchitecture.fieldops.core.common.FeatureFlagManager
import com.stackmyarchitecture.fieldops.core.common.Logger
import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepository
import com.stackmyarchitecture.fieldops.feature.tasks.data.TaskRepositoryContract
import dagger.assisted.Assisted
import dagger.assisted.AssistedInject
import kotlinx.coroutines.flow.first

@HiltWorker
class TaskSyncWorker @AssistedInject constructor(
    @Assisted appContext: Context,
    @Assisted workerParams: WorkerParameters,
    private val taskRepository: TaskRepositoryContract,
    private val logger: Logger,
    private val featureFlagManager: FeatureFlagManager,
) : CoroutineWorker(appContext, workerParams) {

    override suspend fun doWork(): Result {
        val backgroundSyncEnabled = featureFlagManager.isEnabled(FeatureFlag.ENABLE_BACKGROUND_SYNC).first()
        if (!backgroundSyncEnabled) {
            logger.i(TAG, "Background sync disabled by feature flag", emptyMap())
            return Result.success()
        }
        
        logger.i(TAG, "Starting background sync", mapOf(
            "attempt" to runAttemptCount,
            "workerId" to id.toString()
        ))
        
        return try {
            // 1. Push pending local changes
            if (taskRepository is TaskRepository) {
                taskRepository.syncPendingChanges()
            }
            
            // 2. Pull remote changes
            taskRepository.refreshTasks()
            
            logger.i(TAG, "Background sync completed", mapOf("attempt" to runAttemptCount))
            Result.success()
            
        } catch (e: Exception) {
            logger.e(TAG, "Background sync failed", e, mapOf(
                "attempt" to runAttemptCount,
                "maxRetries" to MAX_RETRIES,
                "error" to (e.message ?: "unknown")
            ))
            
            if (runAttemptCount < MAX_RETRIES) {
                logger.w(TAG, "Scheduling retry", metadata = mapOf("nextAttempt" to (runAttemptCount + 1)))
                Result.retry()
            } else {
                logger.e(TAG, "Max retries reached, giving up", metadata = mapOf("attempts" to runAttemptCount))
                Result.failure()
            }
        }
    }

    companion object {
        const val TAG = "TaskSyncWorker"
        const val UNIQUE_WORK_NAME = "task_sync"
        private const val MAX_RETRIES = 3
    }
}
