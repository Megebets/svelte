<script>
  import Header from '../components/Header.svelte';
</script>
  
  <style>
    .archive-container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      font-family: Arial, sans-serif;
    }
  
    .archive-container h1 {
      text-align: center;
      margin-bottom: 20px;
    }
  
    .archive-container p {
      line-height: 1.6;
      font-size: 16px;
    }
  
    .archive-container .content {
      margin-top: 30px;
    }
  </style>
  
    <!-- Хедер -->
    <Header 
      on:openContactModal={() => openModal('contact')} 
      on:openAuthModal={() => openModal('auth')}
      on:openRegistrationModal={() => openModal('registration')}
    />

  <div class="archive-container">
    <h1>Мы</h1>
    <div class="content">
      <p>
        Начало
      </p>
      <p>
        Дата
      </p>
    </div>
  </div>
  