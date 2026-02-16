package com.stackmyarchitecture.fieldops.core.network

import com.google.common.truth.Truth.assertThat
import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import com.stackmyarchitecture.fieldops.core.network.api.FieldOpsApi
import kotlinx.coroutines.test.runTest
import okhttp3.mockwebserver.MockResponse
import okhttp3.mockwebserver.MockWebServer
import org.junit.After
import org.junit.Before
import org.junit.Test
import retrofit2.Retrofit
import retrofit2.converter.moshi.MoshiConverterFactory

class FieldOpsApiTest {

    private lateinit var server: MockWebServer
    private lateinit var api: FieldOpsApi

    @Before
    fun setup() {
        server = MockWebServer()
        server.start()

        val moshi = Moshi.Builder()
            .addLast(KotlinJsonAdapterFactory())
            .build()

        api = Retrofit.Builder()
            .baseUrl(server.url("/"))
            .addConverterFactory(MoshiConverterFactory.create(moshi))
            .build()
            .create(FieldOpsApi::class.java)
    }

    @After
    fun tearDown() {
        server.shutdown()
    }

    @Test
    fun `getTasks returns parsed list from server`() = runTest {
        val json = """
            [
                {"id":"1","title":"Inspeccionar parcela","description":"Verificar riego","status":"open"},
                {"id":"2","title":"Reparar cerca","description":"Tramo dañado","status":"in_progress"}
            ]
        """.trimIndent()

        server.enqueue(MockResponse().setBody(json).setResponseCode(200))

        val tasks = api.getTasks()

        assertThat(tasks).hasSize(2)
        assertThat(tasks[0].id).isEqualTo("1")
        assertThat(tasks[0].title).isEqualTo("Inspeccionar parcela")
        assertThat(tasks[0].status).isEqualTo("open")
        assertThat(tasks[1].id).isEqualTo("2")
        assertThat(tasks[1].status).isEqualTo("in_progress")
    }

    @Test
    fun `getTasks with empty list returns empty`() = runTest {
        server.enqueue(MockResponse().setBody("[]").setResponseCode(200))

        val tasks = api.getTasks()

        assertThat(tasks).isEmpty()
    }

    @Test(expected = Exception::class)
    fun `getTasks with server error throws exception`() = runTest {
        server.enqueue(MockResponse().setResponseCode(500))

        api.getTasks()
    }
}
