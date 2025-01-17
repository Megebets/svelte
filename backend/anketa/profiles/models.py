from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    username = None  # Отключаем стандартное поле username
    phone = models.CharField(max_length=15, unique=True)  # Уникальный номер телефона
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)

    USERNAME_FIELD = 'phone'  # Указываем, что логином будет номер телефона
    REQUIRED_FIELDS = ['last_name', 'first_name', 'middle_name']  # Обязательные поля для создания пользователя

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
