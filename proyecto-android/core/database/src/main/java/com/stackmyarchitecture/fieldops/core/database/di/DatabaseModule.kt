package com.stackmyarchitecture.fieldops.core.database.di

import android.content.Context
import androidx.room.Room
import com.stackmyarchitecture.fieldops.core.database.FieldOpsDatabase
import com.stackmyarchitecture.fieldops.core.database.dao.TaskDao
import com.stackmyarchitecture.fieldops.core.database.migrations.MIGRATION_1_2
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): FieldOpsDatabase {
        return Room.databaseBuilder(
            context,
            FieldOpsDatabase::class.java,
            "fieldops.db",
        )
            .addMigrations(MIGRATION_1_2)
            .build()
    }

    @Provides
    fun provideTaskDao(database: FieldOpsDatabase): TaskDao {
        return database.taskDao()
    }
}
