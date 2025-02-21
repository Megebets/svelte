<script>
  import { goto } from "$app/navigation";

  let formData = {
    phoneNumber: "",
    password: "",
    confirmPassword: ""
  };

  let errors = {
    phoneNumber: "",
    password: "",
    confirmPassword: "",
    server: ""
  };

  let isSubmitting = false;

  function validateForm() {
    errors = { phoneNumber: "", password: "", confirmPassword: "", server: "" };
    const cleanedPhone = formData.phoneNumber.replace(/\D/g, "");
    if (!/^\d{10,15}$/.test(cleanedPhone))
      errors.phoneNumber = "Введите корректный номер телефона.";
    if (!/^(?=.*\d)(?=.*[A-Z]).{6,}$/.test(formData.password))
      errors.password = "Пароль должен содержать цифру и заглавную букву.";
    if (formData.password !== formData.confirmPassword)
      errors.confirmPassword = "Пароли не совпадают.";
    return Object.values(errors).every(e => e === "");
  }

  async function handleSubmit(event) {
    event.preventDefault();
    if (!validateForm()) return;
    isSubmitting = true;
    try {
      const response = await fetch("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });
      if (!response.ok) {
        errors.server = "Ошибка сервера";
        isSubmitting = false;
        return;
      }
      formData = { phoneNumber: "", password: "", confirmPassword: "" };
      goto("/profile");
    } catch {
      errors.server = "Ошибка соединения.";
      isSubmitting = false;
    }
  }
</script>

<div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md mx-auto">
  <h1 class="text-2xl font-bold mb-4 text-center">Регистрация</h1>
  <form on:submit={handleSubmit} class="space-y-4">
    <div>
      <label for="phoneNumber" class="block text-sm font-medium text-gray-700">Номер телефона</label>
      <input
        type="text"
        id="phoneNumber"
        bind:value={formData.phoneNumber}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
      />
      {#if errors.phoneNumber}
        <p class="text-red-500 text-sm mt-1">{errors.phoneNumber}</p>
      {/if}
    </div>
    <div>
      <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
      <input
        type="password"
        id="password"
        bind:value={formData.password}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
      />
      {#if errors.password}
        <p class="text-red-500 text-sm mt-1">{errors.password}</p>
      {/if}
    </div>
    <div>
      <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Подтверждение пароля</label>
      <input
        type="password"
        id="confirmPassword"
        bind:value={formData.confirmPassword}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      {#if errors.confirmPassword}
        <p class="text-red-500 text-sm mt-1">{errors.confirmPassword}</p>
      {/if}
    </div>
    {#if errors.server}
      <p class="text-red-500 text-sm mt-1">{errors.server}</p>
    {/if}
    <button
      type="submit"
      class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-500 transition-colors"
      disabled={isSubmitting}
    >
      {isSubmitting ? "Отправка..." : "Зарегистрироваться"}
    </button>
  </form>
</div>
