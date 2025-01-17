<script>
    let phone = '';
    let lastName = '';
    let firstName = '';
    let middleName = '';
    let password = '';
    let passwordConfirm = '';
    let errorMessage = '';
    
    const handleSubmit = async () => {
      if (password !== passwordConfirm) {
        errorMessage = 'Пароли не совпадают';
        return;
      }
  
      try {
        const response = await fetch('http://localhost:8000/api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            phone,
            last_name: lastName,
            first_name: firstName,
            middle_name: middleName,
            password
          })
        });
  
        if (response.ok) {
          alert('Регистрация успешна');
          // Перенаправление на страницу входа или главную
        } else {
          const errorData = await response.json();
          errorMessage = errorData.detail || 'Ошибка регистрации';
        }
      } catch (error) {
        errorMessage = 'Ошибка сети';
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input bind:value={phone} type="text" placeholder="Номер телефона" required />
    <input bind:value={lastName} type="text" placeholder="Фамилия" required />
    <input bind:value={firstName} type="text" placeholder="Имя" required />
    <input bind:value={middleName} type="text" placeholder="Отчество" required />
    <input bind:value={password} type="password" placeholder="Пароль" required />
    <input bind:value={passwordConfirm} type="password" placeholder="Подтверждение пароля" required />
  
    {#if errorMessage}
      <p style="color: red;">{errorMessage}</p>
    {/if}
  
    <button type="submit">Зарегистрироваться</button>
  </form>