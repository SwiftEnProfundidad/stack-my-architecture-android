package com.stackmyarchitecture.fieldops.core.common

import android.util.Log

interface Logger {
    fun d(tag: String, message: String, metadata: Map<String, Any> = emptyMap())
    fun i(tag: String, message: String, metadata: Map<String, Any> = emptyMap())
    fun w(tag: String, message: String, throwable: Throwable? = null, metadata: Map<String, Any> = emptyMap())
    fun e(tag: String, message: String, throwable: Throwable? = null, metadata: Map<String, Any> = emptyMap())
}

class StructuredLogger : Logger {
    override fun d(tag: String, message: String, metadata: Map<String, Any>) {
        Log.d(tag, formatMessage(message, metadata))
    }

    override fun i(tag: String, message: String, metadata: Map<String, Any>) {
        Log.i(tag, formatMessage(message, metadata))
    }

    override fun w(tag: String, message: String, throwable: Throwable?, metadata: Map<String, Any>) {
        Log.w(tag, formatMessage(message, metadata), throwable)
    }

    override fun e(tag: String, message: String, throwable: Throwable?, metadata: Map<String, Any>) {
        Log.e(tag, formatMessage(message, metadata), throwable)
    }

    private fun formatMessage(message: String, metadata: Map<String, Any>): String {
        if (metadata.isEmpty()) return message
        val metadataStr = metadata.entries.joinToString(", ") { "${it.key}=${it.value}" }
        return "$message | $metadataStr"
    }
}
