<script>
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";

  let formData = {
    phoneNumber: "",
    password: "",
    confirmPassword: "",
  };

  let errors = {
    phoneNumber: "",
    password: "",
    confirmPassword: "",
    server: "",
  };

  let isSubmitting = false;

  function validateForm() {
    errors.phoneNumber = "";
    errors.password = "";
    errors.confirmPassword = "";

    // Проверка номера телефона
    const cleanedPhone = formData.phoneNumber.replace(/\D/g, "");
    if (!/^\d{10,15}$/.test(cleanedPhone)) {
      errors.phoneNumber = "Введите корректный номер телефона.";
    }

    // Проверка пароля
    const passwordRegex = /^(?=.*\d)(?=.*[A-Z]).{6,}$/;
    if (!passwordRegex.test(formData.password)) {
      errors.password = "Пароль должен быть не менее 6 символов, содержать цифру и заглавную букву.";
    }

    // Проверка подтверждения пароля
    if (formData.password !== formData.confirmPassword) {
      errors.confirmPassword = "Пароли не совпадают.";
    }

    return Object.keys(errors).every((key) => errors[key] === "");
  }

  async function handleSubmit(event) {
    event.preventDefault();
    isSubmitting = true;

    if (!validateForm()) {
      isSubmitting = false;
      return;
    }

    try {
      const response = await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const data = await response.json();
        errors.server = data.message || "Ошибка сервера";
        isSubmitting = false;
        return;
      }

      formData = { phoneNumber: "", password: "", confirmPassword: "" };
      goto("/profile");
    } catch (error) {
      errors.server = "Произошла ошибка при отправке данных.";
      isSubmitting = false;
    }
  }
</script>

<div class="min-h-screen bg-gray-100 flex items-center justify-center">
  <div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
    <h1 class="text-2xl font-bold mb-4">Регистрация</h1>
    <form on:submit={handleSubmit}>
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

      <!-- Подтверждение пароля -->
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

      <!-- Кнопка регистрации -->
      <div class="flex justify-end">
        <button
          type="submit"
          class="px-4 py-2 bg-indigo-500 text-white rounded-md hover:bg-indigo-600"
          disabled={isSubmitting}
        >
          {#if isSubmitting}
            Отправка...
          {:else}
            Зарегистрироваться
          {/if}
        </button>
      </div>
    </form>
  </div>
</div>