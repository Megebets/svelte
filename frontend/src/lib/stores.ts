import { writable } from 'svelte/store';
import { browser } from '$app/environment';

// Хранилища
export const userStore = writable(null);
export const archiveStore = writable([]);
export const aboutStore = writable([]);
export const homeStore = writable([]);

// Хранилище для токена
export const tokenStore = writable(browser ? localStorage.getItem('token') || null : null);

// Синхронизация токена с localStorage только на стороне клиента
if (browser) {
  tokenStore.subscribe((value) => {
    if (value) {
      localStorage.setItem('token', value);
    } else {
      localStorage.removeItem('token');
    }
  });
}