package com.stackmyarchitecture.fieldops.core.network.api

import com.stackmyarchitecture.fieldops.core.network.model.NetworkTaskDto
import retrofit2.http.GET

interface FieldOpsApi {

    @GET("tasks")
    suspend fun getTasks(): List<NetworkTaskDto>
}
