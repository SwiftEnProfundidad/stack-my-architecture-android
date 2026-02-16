package com.stackmyarchitecture.fieldops.core.common

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.preferencesDataStore
import dagger.hilt.android.qualifiers.ApplicationContext
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import javax.inject.Inject
import javax.inject.Singleton

private val Context.featureFlagDataStore: DataStore<Preferences> by preferencesDataStore(
    name = "feature_flags"
)

@Singleton
class FeatureFlagDataStore @Inject constructor(
    @ApplicationContext private val context: Context,
) {
    fun getFlag(key: String): Flow<Boolean?> {
        return context.featureFlagDataStore.data.map { prefs ->
            prefs[booleanPreferencesKey(key)]
        }
    }

    suspend fun setFlag(key: String, value: Boolean) {
        context.featureFlagDataStore.edit { prefs ->
            prefs[booleanPreferencesKey(key)] = value
        }
    }

    suspend fun removeFlag(key: String) {
        context.featureFlagDataStore.edit { prefs ->
            prefs.remove(booleanPreferencesKey(key))
        }
    }

    suspend fun clear() {
        context.featureFlagDataStore.edit { prefs ->
            prefs.clear()
        }
    }
}
