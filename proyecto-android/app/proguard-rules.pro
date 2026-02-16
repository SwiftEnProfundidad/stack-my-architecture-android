# FieldOps ProGuard Rules

# Moshi
-keep class com.stackmyarchitecture.fieldops.core.network.model.** { *; }
-keepclassmembers class com.stackmyarchitecture.fieldops.core.network.model.** { *; }

# Retrofit
-dontwarn retrofit2.**
-keep class retrofit2.** { *; }
-keepattributes Signature
-keepattributes Exceptions

# OkHttp
-dontwarn okhttp3.**
-dontwarn okio.**

# Hilt
-keep class dagger.hilt.** { *; }

# Room
-keep class * extends androidx.room.RoomDatabase
