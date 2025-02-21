<script>
  import Registration from './Registration.svelte';
  let activeTab = 'login';

  function handleLogin(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const phoneNumber = formData.get('phoneNumber');
    const password = formData.get('password');
    console.log('Logging in:', { phoneNumber, password });
    // Здесь можно добавить логику для авторизации по номеру телефона
  }
</script>

<div class="min-h-screen bg-gray-100 flex items-center justify-center">
  <div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
    <!-- Переключатель вкладок -->
    <div class="flex border-b mb-4">
      <button
        on:click={() => activeTab = 'login'}
        class="w-1/2 py-2 text-center text-lg font-semibold border-b-2 transition-colors duration-300
          hover:border-blue-500 hover:text-blue-500
          {activeTab === 'login' ? 'border-blue-500 bg-indigo-50 text-blue-500' : 'border-transparent'}"
      >
        Вход
      </button>
      <button
        on:click={() => activeTab = 'register'}
        class="w-1/2 py-2 text-center text-lg font-semibold border-b-2 transition-colors duration-300
          hover:border-blue-500 hover:text-blue-500
          {activeTab === 'register' ? 'border-blue-500 bg-indigo-50 text-blue-500' : 'border-transparent'}"
      >
        Регистрация
      </button>
    </div>

    <!-- Содержимое модального окна -->
    {#if activeTab === 'login'}
      <form on:submit={handleLogin} class="space-y-4">
        <div>
          <label for="phoneNumber" class="block text-sm font-medium text-gray-700">Номер телефона</label>
          <input
            type="text"
            id="phoneNumber"
            name="phoneNumber"
            required
            class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:bg-blue-500"
          />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input
            type="password"
            id="password"
            name="password"
            required
            class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:bg-blue-500"
          />
        </div>
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-500 transition-colors"
        >
          Войти
        </button>
      </form>
    {:else if activeTab === 'register'}
      <Registration />
    {/if}
  </div>
</div>
