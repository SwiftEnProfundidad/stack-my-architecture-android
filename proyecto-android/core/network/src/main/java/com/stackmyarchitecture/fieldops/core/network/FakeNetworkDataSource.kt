package com.stackmyarchitecture.fieldops.core.network

import javax.inject.Inject
import javax.inject.Singleton

@Singleton
class FakeNetworkDataSource @Inject constructor() {

    fun authenticate(email: String, password: String): Boolean {
        return email == "admin@fieldops.com" && password == "fieldops123"
    }

    fun fetchTasks(): List<NetworkTask> {
        return listOf(
            NetworkTask(id = "1", title = "Inspeccionar parcela norte", description = "Verificar estado del riego en sector A", status = "open"),
            NetworkTask(id = "2", title = "Reparar cerca perimetral", description = "Tramo 3 dañado por tormenta", status = "open"),
            NetworkTask(id = "3", title = "Recoger muestras de suelo", description = "Laboratorio requiere 5 muestras del lote B", status = "in_progress"),
            NetworkTask(id = "4", title = "Calibrar sensor de humedad", description = "Sensor H-04 reporta lecturas inconsistentes", status = "done"),
            NetworkTask(id = "5", title = "Actualizar inventario herramientas", description = "Registro mensual obligatorio", status = "open"),
        )
    }
}

data class NetworkTask(
    val id: String,
    val title: String,
    val description: String,
    val status: String,
)
