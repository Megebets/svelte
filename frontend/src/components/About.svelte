<script>
  import Header from '../components/Header.svelte';
  
</script>
  
  <style>
    .about-container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      font-family: Arial, sans-serif;
    }
  
    .about-container h1 {
      text-align: center;
      margin-bottom: 20px;
    }
  
    .about-container p {
      line-height: 1.6;
      font-size: 16px;
    }
  
    .about-container .content {
      margin-top: 30px;
    }
  </style>

  <!-- Хедер -->
  <Header 
    on:openContactModal={() => openModal('contact')} 
    on:openAuthModal={() => openModal('auth')}
    on:openRegistrationModal={() => openModal('registration')}
  />
  
  <div class="about-container">
    <h1>О нас</h1>
    <div class="content">
      <p>
        Мы - команда профессионалов, стремящихся предоставить лучшие решения для наших клиентов. 
        Наша миссия - улучшать ваш опыт и помогать вам достигать поставленных целей.
      </p>
      <p>
        У нас работает опытная команда, готовая справляться с любыми вызовами и предложить вам
        современные и эффективные решения.
      </p>
    </div>
  </div>
  