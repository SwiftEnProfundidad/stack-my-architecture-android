package com.stackmyarchitecture.fieldops.core.database

import androidx.room.Database
import androidx.room.RoomDatabase
import com.stackmyarchitecture.fieldops.core.database.dao.TaskDao
import com.stackmyarchitecture.fieldops.core.database.model.TaskEntity

@Database(
    entities = [TaskEntity::class],
    version = 2,
    exportSchema = true,
)
abstract class FieldOpsDatabase : RoomDatabase() {
    abstract fun taskDao(): TaskDao
}
