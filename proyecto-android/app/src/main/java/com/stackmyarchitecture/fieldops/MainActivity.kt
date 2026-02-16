package com.stackmyarchitecture.fieldops

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.stackmyarchitecture.fieldops.core.ui.theme.FieldOpsTheme
import com.stackmyarchitecture.fieldops.navigation.FieldOpsNavHost
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            FieldOpsTheme {
                FieldOpsNavHost()
            }
        }
    }
}
