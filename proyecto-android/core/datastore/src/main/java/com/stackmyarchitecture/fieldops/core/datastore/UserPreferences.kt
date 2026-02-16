package com.stackmyarchitecture.fieldops.core.datastore

import kotlinx.coroutines.flow.Flow

interface UserPreferences {
    val rememberedEmail: Flow<String>
    val rememberUser: Flow<Boolean>
    suspend fun setRememberedEmail(email: String)
    suspend fun setRememberUser(remember: Boolean)
}
