package com.stackmyarchitecture.fieldops.feature.auth

import com.stackmyarchitecture.fieldops.core.network.NetworkDataSource
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class AuthRepository @Inject constructor(
    private val networkDataSource: NetworkDataSource,
) {
    fun login(email: String, password: String): Boolean {
        return networkDataSource.authenticate(email, password)
    }
}
