plugins {
    alias(libs.plugins.android.library)
}

android {
    namespace = "com.stackmyarchitecture.fieldops.core.testing"
    compileSdk = 36
    defaultConfig { minSdk = 26 }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

}

dependencies {
    api(libs.junit)
    api(libs.truth)
    api(libs.coroutines.test)
    api(libs.turbine)
    implementation(project(":core:common"))
}
