<script>
  import { goto } from '$app/navigation';
  import { tokenStore } from '$lib/stores';

  let formData = {
    phone_number: '', // Используем phone_number для соответствия бэкенду
    password: '',
    confirmPassword: ''
  };

  let errors = {
    phone_number: '',
    password: '',
    confirmPassword: '',
    server: ''
  };

  let isSubmitting = false;

  function validateForm() {
    errors = { phone_number: '', password: '', confirmPassword: '', server: '' };
    const cleanedPhone = formData.phone_number.replace(/\D/g, '');
    if (!/^\d{10,15}$/.test(cleanedPhone)) {
      errors.phone_number = 'Введите корректный номер телефона (10-15 цифр).';
    }
    if (!/^(?=.*\d)(?=.*[A-Z]).{6,}$/.test(formData.password)) {
      errors.password = 'Пароль должен содержать цифру, заглавную букву и быть не короче 6 символов.';
    }
    if (formData.password !== formData.confirmPassword) {
      errors.confirmPassword = 'Пароли не совпадают.';
    }
    return Object.values(errors).every(e => e === '');
  }

  async function handleSubmit(event) {
    event.preventDefault();
    if (!validateForm()) return;

    isSubmitting = true;
    try {
      const response = await fetch('http://localhost:8000/api/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          phone_number: formData.phone_number,
          password: formData.password
        }) // Отправляем только нужные поля
      });

      const data = await response.json();
      if (response.ok) {
        // Предполагаем, что бэкенд возвращает токен после регистрации
        tokenStore.set(data.access || null); // Сохраняем токен, если он есть
        formData = { phone_number: '', password: '', confirmPassword: '' };
        goto('/profile');
      } else {
        errors.server = data.error || 'Ошибка регистрации';
      }
    } catch (err) {
      errors.server = 'Ошибка соединения с сервером.';
      console.error('Registration error:', err);
    } finally {
      isSubmitting = false;
    }
  }
</script>

<div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md mx-auto">
  <h1 class="text-2xl font-bold mb-4 text-center">Регистрация</h1>
  <form on:submit|preventDefault={handleSubmit} class="space-y-4">
    <div>
      <label for="phone_number" class="block text-sm font-medium text-gray-700">Номер телефона</label>
      <input
        type="text"
        id="phone_number"
        bind:value={formData.phone_number}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
        required
      />
      {#if errors.phone_number}
        <p class="text-red-500 text-sm mt-1">{errors.phone_number}</p>
      {/if}
    </div>
    <div>
      <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
      <input
        type="password"
        id="password"
        bind:value={formData.password}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
        required
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
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
        required
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
      class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors"
      disabled={isSubmitting}
    >
      {isSubmitting ? 'Отправка...' : 'Зарегистрироваться'}
    </button>
  </form>
</div>