package com.stackmyarchitecture.fieldops.core.database.model

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "tasks")
data class TaskEntity(
    @PrimaryKey val id: String,
    val title: String,
    val description: String,
    val status: String,
    val createdAt: Long = System.currentTimeMillis(),
    val syncState: String = SyncState.SYNCED.name,
    val lastSyncTimestamp: Long = 0L,
    val localModifiedAt: Long = System.currentTimeMillis(),
)

enum class SyncState {
    SYNCED,
    PENDING_SYNC,
    CONFLICT
}
