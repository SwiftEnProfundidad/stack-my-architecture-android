package com.stackmyarchitecture.fieldops.core.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.stackmyarchitecture.fieldops.core.database.model.TaskEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks ORDER BY createdAt DESC")
    fun observeAll(): Flow<List<TaskEntity>>

    @Query("SELECT * FROM tasks WHERE id = :taskId")
    suspend fun getById(taskId: String): TaskEntity?

    @Query("SELECT * FROM tasks WHERE syncState = 'PENDING_SYNC'")
    suspend fun getPendingSync(): List<TaskEntity>

    @Query("SELECT * FROM tasks WHERE syncState = 'CONFLICT'")
    suspend fun getConflicts(): List<TaskEntity>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsertAll(tasks: List<TaskEntity>)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(task: TaskEntity)

    @Query("UPDATE tasks SET syncState = :syncState, lastSyncTimestamp = :timestamp WHERE id = :taskId")
    suspend fun updateSyncState(taskId: String, syncState: String, timestamp: Long)

    @Query("DELETE FROM tasks")
    suspend fun deleteAll()
}
