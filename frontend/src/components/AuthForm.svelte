<script>
  import Registration from './Registration.svelte';

  let activeTab = 'login'; // Вкладка по умолчанию — "Вход"

  // Обработчик входа
  function handleLogin(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    console.log('Logging in:', { email, password });
    // Добавьте логику отправки данных на сервер
  }
</script>

<div class="min-h-screen bg-gray-100 flex items-center justify-center">
  <div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
    <div class="modal-header">
      <button 
        class={activeTab === 'login' ? 'active' : ''} 
        on:click={() => (activeTab = 'login')}
      >
        Вход
      </button>
      <button 
        class={activeTab === 'register' ? 'active' : ''} 
        on:click={() => (activeTab = 'register')}
      >
        Регистрация
      </button>
    </div>

    <div class="modal-body">
      {#if activeTab === 'login'}
        <!-- Форма входа -->
        <form on:submit={handleLogin}>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required />
          </div>
          <div class="form-group">
            <label for="password">Пароль</label>
            <input type="password" id="password" name="password" required />
          </div>
          <button type="submit">Войти</button>
        </form>
      {:else if activeTab === 'register'}
        <!-- Компонент регистрации -->
        <Registration />
      {/if}
      </div>
  </div>
</div>
