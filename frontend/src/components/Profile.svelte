<script>
  import Header from "../components/Header.svelte";
  import { onMount } from "svelte";

  let isEditing = false;
  let profileCompletion = 0; // Процент заполнения анкеты

  // Данные пользователя
  let userData = {
    full_name: '',
    age: 30,
    has_parents: true,
    birthdate: '',
    birthplace: '',
    number_of_daughters: 0,
    number_of_sons: 0,
    residence: '',
    contact_phone: '',
    trusted_person_phone: '',
    has_housing: false,
    was_married: false,
    height: 170,
    has_criminal_record: false,
    has_bad_habits: false,
    performs_namaz: false,
    clothing_preference: '',
    spouse_nationality_importance: false,
    spouse_age_preference: 30,
    ok_with_divorced_spouse: false,
    willing_to_relocate: false,
    agree_to_be_second_wife: false,
    plan_to_have_children: true,
    health_status: '',
    additional_info: '',
    spouse_requirements: '',
    profile_completion_date: '',
    consent_to_data_processing: false,
    has_children: false,
    children_boys: "",
    children_girls: "",
    children_ages: "",
    education: "",
    education_level: "",
    specialty: "",
    madhhab: "",
  };

  // Категории анкеты
  let categories = [
    {
      title: "Личные данные",
      open: true,
      fields: [
        { key: "full_name", label: "ФИО", type: "text" },
        { key: "age", label: "Возраст", type: "number" },
        { key: "birthdate", label: "Дата рождения", type: "date" },
        { key: "birthplace", label: "Место рождения", type: "text" },
        { key: "residence", label: "Адрес проживания", type: "text" },
        { key: "contact_phone", label: "Контактный телефон", type: "text" },
      ],
    },
    {
      title: "Семейное положение",
      open: false,
      fields: [
        { key: "has_children", label: "Есть ли дети?", type: "checkbox" },
        { key: "number_of_daughters", label: "Количество дочерей", type: "number", condition: userData.has_children },
        { key: "number_of_sons", label: "Количество сыновей", type: "number", condition: userData.has_children },
        { key: "children_ages", label: "Возраст детей", type: "text", condition: userData.has_children },
        { key: "was_married", label: "Был(а) в браке", type: "checkbox" },
      ],
    },
    {
      title: "Образование и работа",
      open: false,
      fields: [
        { key: "education", label: "Образование", type: "select", options: ["", "есть"] },
        { key: "education_level", label: "Уровень образования", type: "select", options: ["", "высшее", "среднее специальное"], condition: userData.education === "есть" },
        { key: "specialty", label: "Специальность", type: "text", condition: userData.education === "есть" && userData.education_level !== "" },
      ],
    },
    {
      title: "Религиозные предпочтения",
      open: false,
      fields: [
        { key: "madhhab", label: "Мазхаб", type: "select", options: ["", "ханафитский", "маликитский", "шафиитский", "ханбалитский"] },
        { key: "performs_namaz", label: "Совершаю намаз", type: "checkbox" },
      ],
    },
    {
      title: "Предпочтения в супруге",
      open: false,
      fields: [
        { key: "spouse_age_preference", label: "Возраст супруга/супруги", type: "number" },
        { key: "spouse_nationality_importance", label: "Важна ли национальность супруга/супруги?", type: "checkbox" },
        { key: "willing_to_relocate", label: "Готов(а) к переезду", type: "checkbox" },
        { key: "agree_to_be_second_wife", label: "Согласна быть второй женой", type: "checkbox" },
      ],
    },
    {
      title: "Дополнительная информация",
      open: false,
      fields: [
        { key: "additional_info", label: "О себе", type: "textarea" },
        { key: "spouse_requirements", label: "Требования к супругу/супруге", type: "textarea" },
      ],
    },
  ];

  // Рассчитываем процент заполнения анкеты
  function calculateCompletion() {
    const requiredFields = [
      "full_name",
      "age",
      "birthdate",
      "birthplace",
      "residence",
      "contact_phone",
      "education",
      "madhhab",
    ];
    const filled = requiredFields.filter((field) => userData[field] !== "" && userData[field] !== null);
    profileCompletion = Math.round((filled.length / requiredFields.length) * 100);
  }

  // Запускаем расчет при загрузке страницы
  onMount(() => {
    calculateCompletion();
  });

  // Валидация формы
  function validateForm() {
    const errors = [];

    if (userData.age < 18) {
      errors.push("Возраст должен быть 18 лет или больше!");
    }
    if (!/^\+?[1-9]\d{1,14}$/.test(userData.contact_phone)) {
      errors.push("Введите корректный номер телефона!");
    }
    if (!userData.full_name.trim()) {
      errors.push("ФИО обязательно для заполнения!");
    }
    if (!userData.birthdate) {
      errors.push("Дата рождения обязательна для заполнения!");
    }

    if (errors.length > 0) {
      alert(errors.join("\n"));
      return false;
    }
    return true;
  }

  // Сохранение профиля
  function saveProfile() {
    if (validateForm()) {
      console.log("Данные отправлены:", userData);
      alert("Анкета сохранена!");
      isEditing = false;
      calculateCompletion();
    }
  }
</script>

<div class="min-h-screen bg-gray-100 flex flex-col">
  <!-- Header -->
  <Header />

  <div class="container mx-auto px-4 py-8">
    <div class="bg-white shadow-lg rounded-lg p-6">
      <h1 class="text-2xl font-bold mb-6">Анкета пользователя</h1>

      <!-- Прогресс-бар -->
      <div class="mb-6">
        <h2 class="text-xl font-bold mb-2">Заполнение анкеты: {profileCompletion}%</h2>
        <div class="bg-gray-200 rounded-full h-2">
          <div class="bg-indigo-500 h-2 rounded-full" style="width: {profileCompletion}%"></div>
        </div>
        {#if profileCompletion < 100}
          <p class="text-sm text-gray-600 mt-2">Заполните обязательные поля: ФИО, возраст, дата рождения.</p>
        {/if}
      </div>

      <!-- Категории -->
      {#each categories as category}
        <div class="mb-6">
          <button on:click={() => (category.open = !category.open)} class="w-full text-left font-semibold text-lg bg-gray-100 p-4 rounded-lg flex items-center justify-between">
            <span>{category.title}</span>
            <svg class="w-6 h-6 transform transition-transform {category.open ? 'rotate-180' : ''}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
            </svg>
          </button>
          {#if category.open}
            <div class="mt-2 p-4 bg-white rounded-lg grid grid-cols-1 md:grid-cols-2 gap-4">
              {#each category.fields as field}
                {#if !field.condition || userData[field.condition.key] === field.condition.value}
                  <div>
                    <label class="block text-sm font-medium text-gray-700">{field.label}</label>
                    {#if field.type === "text" || field.type === "number" || field.type === "date"}
                      <input
                        type={field.type}
                        bind:value={userData[field.key]}
                        class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                      />
                    {:else if field.type === "checkbox"}
                      <label class="inline-flex items-center mt-2">
                        <input type="checkbox" bind:checked={userData[field.key]} class="form-checkbox h-5 w-5 text-indigo-600" />
                        <span class="ml-2 text-gray-700">{field.label}</span>
                      </label>
                    {:else if field.type === "select"}
                      <select bind:value={userData[field.key]} class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                        {#each field.options as option}
                          <option value={option}>{option || "Выберите"}</option>
                        {/each}
                      </select>
                    {:else if field.type === "textarea"}
                      <textarea bind:value={userData[field.key]} class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring-indigo-500"></textarea>
                    {/if}
                  </div>
                {/if}
              {/each}
            </div>
          {/if}
        </div>
      {/each}

      <!-- Кнопки -->
      <div class="flex justify-end gap-4 mt-6">
        <button type="button" class="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600 transition-colors" on:click={() => (isEditing = false)}>
          Отмена
        </button>
        <button type="button" class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 transition-colors" on:click={saveProfile}>
          Сохранить
        </button>
      </div>
    </div>
  </div>
</div>