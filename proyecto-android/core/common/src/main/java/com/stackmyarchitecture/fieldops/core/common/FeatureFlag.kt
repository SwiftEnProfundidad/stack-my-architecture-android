package com.stackmyarchitecture.fieldops.core.common

enum class FeatureFlag(val key: String, val defaultValue: Boolean) {
    ENABLE_OFFLINE_SYNC("enable_offline_sync", true),
    ENABLE_BACKGROUND_SYNC("enable_background_sync", true),
    ENABLE_CONFLICT_RESOLUTION("enable_conflict_resolution", true),
    ENABLE_ADVANCED_LOGGING("enable_advanced_logging", false),
    ENABLE_TASK_FILTERS("enable_task_filters", false),
    ENABLE_BETA_FEATURES("enable_beta_features", false),
}
