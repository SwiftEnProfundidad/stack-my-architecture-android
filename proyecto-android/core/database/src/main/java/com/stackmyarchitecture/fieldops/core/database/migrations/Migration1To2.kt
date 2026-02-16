package com.stackmyarchitecture.fieldops.core.database.migrations

import androidx.room.migration.Migration
import androidx.sqlite.db.SupportSQLiteDatabase

val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE tasks ADD COLUMN syncState TEXT NOT NULL DEFAULT 'SYNCED'")
        db.execSQL("ALTER TABLE tasks ADD COLUMN lastSyncTimestamp INTEGER NOT NULL DEFAULT 0")
        db.execSQL("ALTER TABLE tasks ADD COLUMN localModifiedAt INTEGER NOT NULL DEFAULT 0")
    }
}
