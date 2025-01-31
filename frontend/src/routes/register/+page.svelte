<script>
  import { onMount } from "svelte";
  import { goto } from "$app/navigation"; // Для перенаправления после успешной регистрации.

  let formData = {
    fullName: "",
    phoneNumber: "",
    password: "",
    confirmPassword: ""
  };

  let errors = {};

  function validateForm() {
    errors = {};

    // Проверка полного имени
    if (!formData.fullName.trim()) {
      errors.fullName = "Полное имя обязательно.";
    }

    // Проверка номера телефона
    const phoneRegex = /^\+?[1-9]\d{1,14}$/;
    if (!phoneRegex.test(formData.phoneNumber)) {
      errors.phoneNumber = "Введите корректный номер телефона.";
    }

    // Проверка пароля
    if (formData.password.length < 6) {
      errors.password = "Пароль должен быть не менее 6 символов.";
    }

    // Проверка подтверждения пароля
    if (formData.password !== formData.confirmPassword) {
      errors.confirmPassword = "Пароли не совпадают.";
    }

    return Object.keys(errors).length === 0;
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (!validateForm()) {
      return;
    }

    // Отправляем данные на сервер
    try {
      const response = await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        const data = await response.json();
        errors.server = data.message || "Ошибка регистрации. Попробуйте позже.";
        return;
      }

      // Перенаправляем на страницу личного кабинета
      goto("/profile");
    } catch (err) {
      errors.server = "Ошибка подключения к серверу.";
    }
  }
</script>

<div class="min-h-screen bg-gray-100 flex items-center justify-center">
  <div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
    <h1 class="text-2xl font-bold mb-4">Регистрация</h1>
    <form on:submit={handleSubmit}>
      <!-- Полное имя -->
      <div class="mb-4">
        <label for="fullName" class="block text-sm font-medium text-gray-700">Полное имя</label>
        <input
          type="text"
          id="fullName"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          bind:value={formData.fullName}
        />
        {#if errors.fullName}
          <p class="text-red-500 text-sm mt-1">{errors.fullName}</p>
        {/if}
      </div>

      <!-- Номер телефона -->
      <div class="mb-4">
        <label for="phoneNumber" class="block text-sm font-medium text-gray-700">Номер телефона</label>
        <input
          type="text"
          id="phoneNumber"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          bind:value={formData.phoneNumber}
        />
        {#if errors.phoneNumber}
          <p class="text-red-500 text-sm mt-1">{errors.phoneNumber}</p>
        {/if}
      </div>

      <!-- Пароль -->
      <div class="mb-4">
        <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
        <input
          type="password"
          id="password"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          bind:value={formData.password}
        />
        {#if errors.password}
          <p class="text-red-500 text-sm mt-1">{errors.password}</p>
        {/if}
      </div>

      <!-- Подтверждение пароля--> 
      <div class="mb-4">
        <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Подтверждение пароля</label>
        <input
          type="password"
          id="confirmPassword"
          class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          bind:value={formData.confirmPassword}
        />
        {#if errors.confirmPassword}
          <p class="text-red-500 text-sm mt-1">{errors.confirmPassword}</p>
        {/if}
      </div>

      <!-- Ошибка сервера -->
      {#if errors.server}
        <p class="text-red-500 text-sm mb-4">{errors.server}</p>
      {/if}

      <!-- Кнопка регистрации  -->
      <div class="flex justify-end">
        <button
          type="submit"
          class="px-4 py-2 bg-indigo-500 text-white rounded-md hover:bg-indigo-600"
        >
          Зарегистрироваться
        </button>
      </div>
    </form>
  </div>
</div>
 