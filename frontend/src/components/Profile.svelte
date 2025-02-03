<script>
	import Header from '../components/Header.svelte';
	import { onMount } from 'svelte';
	let isEditing = false;
	let profileCompletion = 0; // Процент заполнения анкеты
	let userData = {
		last_name: '',
		name: '',
		middle_name: '',
		age: 30,
		has_parents: '',
    livingplace: '',
		birthdate: '',
		birthplace: '',
		number_of_daughters: 0,
		number_of_sons: 0,
		residence: '',
		contact_phone: '',
		trusted_person_phone: '',
    has_working: '',
		has_housing: '',
		was_married: '',
		height: 170,
		has_criminal_record: false,
		has_bad_habits: '',
		performs_namaz: '',
		clothing_preference: '',
		spouse_nationality_importance: false,
		spouse_age_preference: 30,
		ok_with_divorced_spouse: false,
    ok_with_spouse_children: '',
		willing_to_relocate: false,
		agree_to_be_second_wife: false,
		plan_to_have_children: true,
		health_status: '',
		additional_info: '',
		spouse_requirements: '',
		profile_completion_date: '',
		consent_to_data_processing: false,
		has_children: false,
		children_boys: '',
		children_girls: '',
		children_ages: '',
		education: '',
		education_level: '',
		specialty: '',
		madhhab: ''
	};
	function saveProfile() {
		console.log('Данные отправлены:', userData);
		// Здесь можно добавить отправку данных на сервер
	}

	// Рассчитываем процент заполнения анкеты
	function calculateCompletion() {
		const fields = Object.values(userData);
		const filled = fields.filter((value) => value !== '' && value !== null);
		profileCompletion = Math.round((filled.length / fields.length) * 100);
	}

	// Запускаем расчет при загрузке страницы
	onMount(() => {
		calculateCompletion();
	});

	// Пример валидации
	function validateForm() {
		if (userData.age < 18) {
			alert('Возраст должен быть 18 лет или больше!');
			return false;
		}
		if (!/^\+?[1-9]\d{1,14}$/.test(userData.contactPhone)) {
			alert('Введите корректный номер телефона!');
			return false;
		}
		return true;
	}

	//   function saveProfile() {
	//     if (validateForm()) {
	//       alert("Анкета сохранена!");
	//       isEditing = false;
	//       calculateCompletion();
	//     }
	//   }
</script>

<div class="flex min-h-screen flex-col bg-gray-100">
	<!-- Header visible on all pages -->
	<Header />
	<div class="container mx-auto flex items-center justify-between px-4 py-4">
		<div class="flex items-center gap-4">
			<div class="rounded-[50%] bg-gray-300">
				<img src={userData.avatar} alt="" class="h-16 w-16 rounded-full object-cover" />
			</div>
			<div>
				<h1 class="text-2xl font-bold">{userData.fullName}</h1>
				<p class="text-sm text-gray-500">Ваш личный кабинет</p>
			</div>
		</div>
		<button class="rounded bg-red-500 px-4 py-2 text-white">Выход</button>
	</div>

	<main class="container mx-auto grid flex-grow grid-cols-1 gap-8 px-4 py-8 md:grid-cols-3">
		<!-- Анкета -->
		<div class="col-span-2 rounded-lg bg-white p-6 shadow">
			<h2 class="mb-4 text-xl font-bold">Анкета</h2>

			{#if isEditing}
				<form class="mx-auto max-w-2xl rounded-md bg-white p-6 shadow-md">
					<h2 class="mb-4 text-xl font-semibold">Анкета пользователя</h2>

					<div class="grid grid-cols-1 gap-4">
						<div>
							<label class="block text-sm font-medium text-gray-700">Фамилия</label>
							<input
								type="text"
								bind:value={userData.last_name}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Имя</label>
							<input
								type="text"
								bind:value={userData.name}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Отчество</label>
							<input
								type="text"
								bind:value={userData.middle_name}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Возраст</label>
							<input
								type="number"
								bind:value={userData.age}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Дата рождения</label>
							<input
								type="date"
								bind:value={userData.birthdate}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Место рождения</label>
							<input
								type="text"
								bind:value={userData.birthplace}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Национальность</label>
							<input
								type="text"
								bind:value={userData.birthplace}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Адрес проживания</label>
							<input
								type="text"
								bind:value={userData.birthplace}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Контактный телефон</label>
							<input
								type="text"
								bind:value={userData.contact_phone}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Телефон доверенного лица</label
							>
							<input
								type="text"
								bind:value={userData.trusted_person_phone}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700">Рост (см)</label>
							<input
								type="number"
								bind:value={userData.height}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<!-- Вопрос: имеются ли дети? -->
						<div>
							<label class="block text-sm font-medium text-gray-700">Имеются ли дети?</label>
							<select
								bind:value={userData.has_children}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Да</option>
							</select>
						</div>

						{#if userData.has_children}
							<div>
								<label class="block text-sm font-medium text-gray-700">Сколько мальчиков?</label>
								<input
									type="number"
									bind:value={userData.children_boys}
									class="mt-1 block w-full rounded-md border-gray-300"
								/>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-700">Сколько девочек?</label>
								<input
									type="number"
									bind:value={userData.children_girls}
									class="mt-1 block w-full rounded-md border-gray-300"
								/>
							</div>

							<div>
								<label class="block text-sm font-medium text-gray-700">Возраст детей</label>
								<input
									type="text"
									bind:value={userData.children_ages}
									class="mt-1 block w-full rounded-md border-gray-300"
									placeholder="Например: 5, 7, 10"
								/>
							</div>
						{/if}

						<!-- Вопрос: образование -->
						<div>
							<label class="block text-sm font-medium text-gray-700">Образование</label>
							<select
								bind:value={userData.education}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value="">Нет</option>
								<option value="есть">Есть</option>
							</select>
						</div>

						{#if userData.education === 'есть'}
							<div>
								<label class="block text-sm font-medium text-gray-700">Какой уровень?</label>
								<select bind:value={userData.education_level} class="mt-1 block w-full rounded-md border-gray-300">
									<option value="высшее">Высшее</option>
									<option value="среднее специальное">Среднее специальное</option>
								</select>
							</div>

							{#if userData.education_level !== ''}
								<div>
									<label class="block text-sm font-medium text-gray-700">Специальность</label>
									<input
										type="text"
										bind:value={userData.specialty}
										class="mt-1 block w-full rounded-md border-gray-300"
									/>
								</div>
							{/if}
						{/if}

						<!-- Вопрос: мазхаб -->
						<div>
							<label class="block text-sm font-medium text-gray-700">Какого мазхаба придерживаетесь?</label>
							<select bind:value={userData.madhhab} class="mt-1 block w-full rounded-md border-gray-300">
								<option value="ханафитский">Ханафитский</option>
								<option value="маликитский">Маликитский</option>
								<option value="шафиитский">Шафиитский</option>
								<option value="ханбалитский">Ханбалитский</option>
							</select>
						</div>

            <div>
              <label class="block text-sm font-medium text-gray-700">У вас есть собственное жилье?</label>
              <select bind:value={userData.has_housing} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Есть">Есть</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700">У вас есть родители?</label>
              <select bind:value={userData.has_parents} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Есть">Есть</option>
                <option value="Нет">Нет</option>
              </select>
                {#if userData.has_parents === 'Есть'}
                  <div>
                    <label class="block text-sm font-medium text-gray-700">Вы проживайте с родителями?</label>
                    <select bind:value={userData.livingplace} class="mt-1 block w-full rounded-md border-gray-300" >
                      <option value="Я проживаю с родителями">Я проживаю с родителями</option>
                      <option value="Я живу один">Я живу один</option>
                    </select>
                  </div>
                {/if}
            </div>
            <div> 
              <label class="block text-sm font-medium text-gray-700">Вы работайте?</label>
              <select bind:value={userData.has_working} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Работаю">Работаю</option>
                <option value="Не работаю">Не работаю</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Вы состояли в браке?</label>
              <select bind:value={userData.was_married} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">У вас есть судимость?</label>
              <select bind:value={userData.has_criminal_record} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Есть">Есть</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Вы совершайте намаз?</label>
              <select bind:value={userData.has_criminal_record} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Какие вредные привычки присуши вам?</label>
              <input
								type="text"
								bind:value={userData.has_bad_habits}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Возможен брак с разведённым(ой)?</label>
              <select bind:value={userData.ok_with_divorced_spouse} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Возможен ли брак с человеком у каторого есть дети?</label>
              <select bind:value={userData.ok_with_spouse_children} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Готовы ли к переезду?</label>
              <select bind:value={userData.willing_to_relocate} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>
    
            <div> 
              <label class="block text-sm font-medium text-gray-700">Согласна быть второй женой?</label>
              <select bind:value={userData.agree_to_be_second_wife} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

            <div> 
              <label class="block text-sm font-medium text-gray-700">Планируйте детей?</label>
              <select bind:value={userData.plan_to_have_children} class="mt-1 block w-full rounded-md border-gray-300" >
                <option value="Да">Да</option>
                <option value="Нет">Нет</option>
              </select>
            </div>

						

						<div>
							<label class="block text-sm font-medium text-gray-700"
								>Ваши предпочтения в одежде:
							</label>
							<input
								type="text"
								bind:value={userData.education}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700"
								>Возвраст будещего(ей) супруга(и)?</label
							>
							<input
								type="text"
								bind:value={userData.education}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div>
							<label class="block text-sm font-medium text-gray-700"
								>Состояние вашего здоровья:
							</label>
							<input
								type="text"
								bind:value={userData.education}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<!-- Текстовые поля -->
						<div class="mt-4">
							<label class="block text-sm font-medium text-gray-700">О себе</label>
							<textarea
								bind:value={userData.additional_info}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							></textarea>
						</div>

						<div class="mt-4">
							<label class="block text-sm font-medium text-gray-700">Требования к супругу</label>
							<textarea
								bind:value={userData.spouse_requirements}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							></textarea>
						</div>

						<!-- Кнопки -->
						<div class="mt-6 flex justify-end gap-4">

              <!-- Чекбоксы -->
              <div class="mt-4 grid grid-cols-1 gap-4 md:grid-cols-2">
                {#each [ { key: 'consent_to_data_processing', label: 'Согласен(а) на обработку персональных данных' }] as item}
                  <div>
                    <label class="inline-flex items-center">
                      <input
                        type="checkbox"
                        bind:checked={userData[item.key]}
                        class="form-checkbox h-5 w-5 text-indigo-600"
                      />
                      <span class="ml-2 text-gray-700">{item.label}</span>
                    </label>
                  </div>
                {/each}
              </div>

							<button
								type="button"
								class="rounded bg-gray-500 px-4 py-2 text-white"
								on:click={() => (userData = {})}
							>
								Отмена
							</button>
							<button
								type="button"
								class="rounded bg-green-500 px-4 py-2 text-white"
								on:click={saveProfile}
							>
								Сохранить
							</button>
						</div>
					</div>
				</form>
			{:else}
				<p class="mb-4 text-gray-700">
					Ваш возраст: {userData.age} <br />
					Контактный телефон: {userData.contactPhone || 'Не указан'}
				</p>
				<button
					class="rounded bg-blue-500 px-4 py-2 text-white"
					on:click={() => (isEditing = true)}
				>
					Редактировать анкету
				</button>
			{/if}
			<!-- Процент заполнения -->
			<div class="container mx-auto rounded-lg bg-white px-4 py-8 shadow">
				<h2 class="mb-4 text-xl font-bold">Заполнение анкеты</h2>
				<div class="relative pt-1">
					<div class="mb-2 flex items-center justify-between">
						<span
							class="inline-block rounded-full bg-indigo-200 px-2 py-1 text-xs font-semibold uppercase text-indigo-600"
						>
							{profileCompletion}%
						</span>
					</div>
					<div class="mb-4 flex h-2 overflow-hidden rounded bg-indigo-200 text-xs">
						<div
							style="width: {profileCompletion}%"
							class="flex flex-col justify-center whitespace-nowrap bg-indigo-500 text-center text-white shadow-none"
						></div>
					</div>
				</div>
			</div>
		</div>

		<!-- Поле для скроллинга анкет -->
		<div class="rounded-lg bg-white p-6 shadow">
			<h2 class="mb-4 text-xl font-bold">Другие анкеты</h2>
			<div class="h-64 overflow-y-auto">
				<!-- Пример данных -->
				<p class="mb-2 text-gray-700">Анкета 1</p>
				<p class="mb-2 text-gray-700">Анкета 2</p>
				<p class="mb-2 text-gray-700">Анкета 3</p>
			</div>
		</div>
	</main>

	<div class="container mx-auto px-4 py-8">
		<div class="rounded-lg bg-white p-6 shadow">
			<div class="h-64 overflow-y-auto">
				Здесь будут полезные советы, для тех кто собирается создать семью
				<p class="mb-2 text-gray-700">Будь мягок со своей семьей</p>
			</div>
		</div>
	</div>
</div>
