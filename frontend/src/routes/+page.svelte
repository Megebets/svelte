<script>
  import Header from '../components/Header.svelte';
  import Footer from '../components/Footer.svelte';
  import Modal from '../components/Modal.svelte';
  import ContactInfo from '../components/ContactInfo.svelte';
  import AuthForm from '../components/AuthForm.svelte';
  import Registration from '../components/Registration.svelte';

  let activeModal = ''; // Хранит текущий открытый модальный тип ('contact', 'auth', 'registration')

  const openModal = (type) => {
    activeModal = type;
  };

  const closeModal = () => {
    activeModal = '';
  };
</script>

<div class="flex flex-col min-h-screen bg-gray-50">
  <!-- Хедер -->
  <Header 
    on:openContactModal={() => openModal('contact')} 
    on:openAuthModal={() => openModal('auth')}
    on:openRegistrationModal={() => openModal('registration')}
  />

  <!-- Основной контент -->
  <main class="flex-grow p-6 bg-white">
    <!-- Секция карусели -->
    <section class="mb-10">
      <h2 class="text-2xl font-bold text-gray-800 mb-4">Карусель слайдов</h2>
      <div class="bg-gray-200 h-64 rounded-lg flex items-center justify-center text-gray-500">
        Здесь будет карусель...
      </div>
    </section>

    <!-- Секция новостей -->
    <section class="mb-10">
      <h2 class="text-2xl font-bold text-gray-800 mb-4">Последние новости</h2>
      <div class="space-y-4">
        <div class="bg-gray-100 p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-700">Новость 1</h3>
          <p class="text-gray-600">Краткое описание новости.</p>
        </div>
        <div class="bg-gray-100 p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-700">Новость 2</h3>
          <p class="text-gray-600">Краткое описание новости.</p>
        </div>
      </div>
    </section>

    <!-- Секция статей -->
    <section>
      <h2 class="text-2xl font-bold text-gray-800 mb-4">Популярные статьи</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-gray-100 p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-700">Статья 1</h3>
          <p class="text-gray-600">Краткое описание статьи.</p>
        </div>
        <div class="bg-gray-100 p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-700">Статья 2</h3>
          <p class="text-gray-600">Краткое описание статьи.</p>
        </div>
      </div>
    </section>
  </main>

  <!-- Футер -->
  <Footer />

  <!-- Модальное окно для контактов -->
  {#if activeModal === 'contact'}
    <Modal on:close={closeModal}>
      <ContactInfo />
    </Modal>
  {/if}

  <!-- Модальное окно для авторизации -->
  {#if activeModal === 'auth'}
    <Modal on:close={closeModal}>
      <AuthForm />
    </Modal>
  {/if}

  <!-- Модальное окно для регистрации -->
  {#if activeModal === 'registration'}
    <Modal on:close={closeModal}>
      <Registration />
    </Modal>
  {/if}
</div>
