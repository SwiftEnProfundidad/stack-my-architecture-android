package com.stackmyarchitecture.fieldops.core.datastore

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import dagger.hilt.android.qualifiers.ApplicationContext
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import javax.inject.Inject
import javax.inject.Singleton

private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "user_prefs")

@Singleton
class UserPreferencesDataStore @Inject constructor(
    @ApplicationContext private val context: Context,
) : UserPreferences {
    private object Keys {
        val REMEMBERED_EMAIL = stringPreferencesKey("remembered_email")
        val REMEMBER_USER = booleanPreferencesKey("remember_user")
    }

    override val rememberedEmail: Flow<String> = context.dataStore.data.map { prefs ->
        prefs[Keys.REMEMBERED_EMAIL] ?: ""
    }

    override val rememberUser: Flow<Boolean> = context.dataStore.data.map { prefs ->
        prefs[Keys.REMEMBER_USER] ?: false
    }

    override suspend fun setRememberedEmail(email: String) {
        context.dataStore.edit { prefs -> prefs[Keys.REMEMBERED_EMAIL] = email }
    }

    override suspend fun setRememberUser(remember: Boolean) {
        context.dataStore.edit { prefs -> prefs[Keys.REMEMBER_USER] = remember }
    }
}
