package com.stackmyarchitecture.rutinadiaria.screens

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun RutinaScreen(onRutinaValida: (String) -> Unit) {
    var nombre by remember { mutableStateOf("") }
    var error by remember { mutableStateOf<String?>(null) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp),
    ) {
        Text(
            text = "Crea tu rutina",
            style = MaterialTheme.typography.headlineSmall,
        )
        Text(
            text = "Escribe un nombre para tu rutina diaria. Debe tener al menos 3 caracteres.",
            style = MaterialTheme.typography.bodyMedium,
        )
        OutlinedTextField(
            value = nombre,
            onValueChange = {
                nombre = it
                error = null
            },
            label = { Text("Nombre de la rutina") },
            isError = error != null,
            supportingText = { error?.let { Text(it) } },
            modifier = Modifier.fillMaxWidth(),
        )
        Button(
            onClick = {
                if (nombre.length < 3) {
                    error = "El nombre debe tener al menos 3 caracteres"
                } else {
                    onRutinaValida(nombre)
                }
            },
            modifier = Modifier.fillMaxWidth(),
        ) {
            Text("Guardar rutina")
        }
    }
}
