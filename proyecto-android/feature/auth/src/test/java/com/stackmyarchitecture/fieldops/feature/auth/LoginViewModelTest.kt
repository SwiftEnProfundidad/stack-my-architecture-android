package com.stackmyarchitecture.fieldops.feature.auth

import com.stackmyarchitecture.fieldops.core.datastore.UserPreferences
import com.stackmyarchitecture.fieldops.core.network.NetworkDataSource
import com.stackmyarchitecture.fieldops.core.network.model.NetworkTaskDto
import com.stackmyarchitecture.fieldops.core.testing.MainDispatcherRule
import com.google.common.truth.Truth.assertThat
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.test.runTest
import org.junit.Before
import org.junit.Rule
import org.junit.Test

class LoginViewModelTest {

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    private lateinit var viewModel: LoginViewModel
    private lateinit var authRepository: AuthRepository
    private lateinit var fakePrefs: FakeUserPreferences

    @Before
    fun setup() {
        authRepository = AuthRepository(FakeTestNetworkDataSource())
        fakePrefs = FakeUserPreferences()
        viewModel = LoginViewModel(authRepository, fakePrefs)
    }

    @Test
    fun `initial state has empty fields`() {
        val state = viewModel.uiState.value
        assertThat(state.email).isEmpty()
        assertThat(state.password).isEmpty()
        assertThat(state.isLoading).isFalse()
        assertThat(state.errorMessage).isNull()
    }

    @Test
    fun `onEmailChange updates email in state`() {
        viewModel.onEmailChange("test@example.com")
        assertThat(viewModel.uiState.value.email).isEqualTo("test@example.com")
    }

    @Test
    fun `onPasswordChange updates password in state`() {
        viewModel.onPasswordChange("secret123")
        assertThat(viewModel.uiState.value.password).isEqualTo("secret123")
    }

    @Test
    fun `login with blank fields sets error`() {
        var loginCalled = false
        viewModel.login { loginCalled = true }
        assertThat(viewModel.uiState.value.errorMessage).isEqualTo("Email y contraseña requeridos")
        assertThat(loginCalled).isFalse()
    }

    @Test
    fun `login with valid credentials calls onSuccess`() = runTest {
        var loginSuccess = false
        viewModel.onEmailChange("admin@fieldops.com")
        viewModel.onPasswordChange("fieldops123")
        viewModel.login { loginSuccess = true }
        assertThat(loginSuccess).isTrue()
        assertThat(viewModel.uiState.value.errorMessage).isNull()
    }

    @Test
    fun `login with invalid credentials sets error message`() = runTest {
        var loginSuccess = false
        viewModel.onEmailChange("wrong@example.com")
        viewModel.onPasswordChange("wrong")
        viewModel.login { loginSuccess = true }
        assertThat(loginSuccess).isFalse()
        assertThat(viewModel.uiState.value.errorMessage).isEqualTo("Credenciales inválidas")
    }
}

private class FakeUserPreferences : UserPreferences {
    private val _email = MutableStateFlow("")
    private val _remember = MutableStateFlow(false)

    override val rememberedEmail: Flow<String> = _email
    override val rememberUser: Flow<Boolean> = _remember

    override suspend fun setRememberedEmail(email: String) { _email.value = email }
    override suspend fun setRememberUser(remember: Boolean) { _remember.value = remember }
}

private class FakeTestNetworkDataSource : NetworkDataSource {
    override suspend fun fetchTasks(): List<NetworkTaskDto> = emptyList()
    override fun authenticate(email: String, password: String): Boolean {
        return email == "admin@fieldops.com" && password == "fieldops123"
    }
}
