package com.stackmyarchitecture.fieldops.core.network

import com.stackmyarchitecture.fieldops.core.network.api.FieldOpsApi
import com.stackmyarchitecture.fieldops.core.network.model.NetworkTaskDto
import javax.inject.Inject
import javax.inject.Singleton

interface NetworkDataSource {
    suspend fun fetchTasks(): List<NetworkTaskDto>
    fun authenticate(email: String, password: String): Boolean
}

@Singleton
class RetrofitNetworkDataSource @Inject constructor(
    private val api: FieldOpsApi,
    private val fallback: FakeNetworkDataSource,
) : NetworkDataSource {

    override suspend fun fetchTasks(): List<NetworkTaskDto> {
        return try {
            api.getTasks()
        } catch (_: Exception) {
            fallback.fetchTasks().map { net ->
                NetworkTaskDto(
                    id = net.id,
                    title = net.title,
                    description = net.description,
                    status = net.status,
                )
            }
        }
    }

    override fun authenticate(email: String, password: String): Boolean {
        return fallback.authenticate(email, password)
    }
}
