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

<div class="modal">
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

<style>
  .modal-header button {
    margin-right: 10px;
    padding: 10px;
    cursor: pointer;
  }

  .modal-header button.active {
    font-weight: bold;
    border-bottom: 2px solid #007bff;
  }

  .modal-body {
    padding: 20px;
  }

  .form-group {
    margin-bottom: 15px;
  }

  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  .form-group input {
    width: 100%; /* Ширина 100% */
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box; /* Учитывает padding в ширине */
  }

  button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>