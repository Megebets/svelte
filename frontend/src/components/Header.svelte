<script>
  import AuthModal from './AuthForm.svelte';
  let showModal = false; // Состояние модального окна
  let showMenu = false;
</script>

<header>
  <section class="flex justify-between bg-gray-800 text-white p-4">
    <!-- Логотип -->
    <div class="flex items-center">
      <img src="/images/logo.jpg" alt="Логотип моего сайта" class="h-16 w-16">
    </div>

    <!-- Название и описание -->
    <div class="flex flex-col text-center mx-auto">
      <h1 class="text-2xl font-bold whitespace-nowrap">"УЮТ"</h1>
      <h2 class="text-lg text-gray-300 whitespace-nowrap">Институт семейного счастья</h2>
    </div>
    
    <button
    class="block md:hidden bg-gray-700 p-2 rounded"
    on:click={() => (showMenu = !showMenu)}
  >
    ☰
  </button>

    <!-- Навигация -->
    <nav>
      <ul class="flex space-x-6 text-base">
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/" >
            Главная
          </a>
        </li>
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/contacts" >
            Контакты
          </a>
        </li>
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/about" >
            О нас
          </a>
        </li>
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/archive" >
            Архив
          </a>
        </li>
        <li class="bg-blue-500 hover:text-green-200 text-white px-6 py-2 rounded-lg hover:scale-105 transition duration-200">
          <button on:click={() => (showModal = true)}>
            Войти
          </button>
        </li>
      </ul>
    </nav>
  </section>
</header>

<style>
  @media (max-width: 768px) {
  header {
    flex-direction: column;
    align-items: center;
  }

  nav ul {
    flex-direction: column;
    gap: 1rem;
  }
}

</style>