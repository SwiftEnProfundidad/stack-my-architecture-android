package com.stackmyarchitecture.fieldops.core.network.model

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class NetworkTaskDto(
    val id: String,
    val title: String,
    val description: String,
    val status: String,
)
