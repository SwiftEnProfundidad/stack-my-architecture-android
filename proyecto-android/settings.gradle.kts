pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "FieldOps"

include(":app")
include(":core:common")
include(":core:ui")
include(":core:testing")
include(":core:network")
include(":core:database")
include(":core:datastore")
include(":feature:onboarding")
include(":feature:auth")
include(":feature:catalog")
include(":feature:tasks")
include(":benchmark")
include(":baselineprofile")
