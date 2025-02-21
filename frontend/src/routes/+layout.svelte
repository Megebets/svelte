<svelte:head>
  <link rel="icon" href="/favicon.png" type="image/png" />
</svelte:head>

<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store'; // Добавляем импорт writable
  import { goto } from '$app/navigation';
  import { userStore, tokenStore, archiveStore, aboutStore } from '$lib/stores';
  import Header from '../components/Header.svelte';
  import Footer from '../components/Footer.svelte';

  let loading = true;

  // Добавим хранилище для главной страницы
  export const homeStore = writable([]); // Теперь writable определён
  $: homeData = $homeStore;

  async function loadData() {
    const token = $tokenStore;
    if (!token) {
      goto('/login');
      return;
    }

    try {
      const sections = ['home', 'about', 'archive'];
      for (const section of sections) {
        const response = await fetch(`http://localhost:8000/api/${section}/`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!response.ok) throw new Error(`Ошибка загрузки ${section}`);
        const data = await response.json();
        if (section === 'home') homeStore.set(data);
        if (section === 'about') aboutStore.set(data);
        if (section === 'archive') archiveStore.set(data);
      }

      const userResponse = await fetch('http://localhost:8000/api/profile/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!userResponse.ok) throw new Error('Ошибка загрузки профиля');
      userStore.set(await userResponse.json());
    } catch (error) {
      console.error(error);
      goto('/login');
    } finally {
      loading = false;
    }
  }

  onMount(loadData);
</script>

{#if loading}
  <div class="flex justify-center items-center min-h-screen">Загрузка...</div>
{:else}
  <div class="flex flex-col min-h-screen bg-gray-100">
    <Header />
    <slot />
    <Footer />
  </div>
{/if}