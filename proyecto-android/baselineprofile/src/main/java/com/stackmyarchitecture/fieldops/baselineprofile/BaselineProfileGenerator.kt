package com.stackmyarchitecture.fieldops.baselineprofile

import androidx.benchmark.macro.junit4.BaselineProfileRule
import org.junit.Rule
import org.junit.Test

class BaselineProfileGenerator {

    @get:Rule
    val rule = BaselineProfileRule()

    @Test
    fun generateBaselineProfile() {
        rule.collect(
            packageName = "com.stackmyarchitecture.fieldops",
        ) {
            pressHome()
            startActivityAndWait()
        }
    }
}
