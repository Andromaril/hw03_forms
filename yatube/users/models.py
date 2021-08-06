from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUp(models.Model):
    """Описывает поля модели SignUp и их типы."""

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        """Для вывода имени пользователя"""

        return self.username
