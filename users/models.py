from django.contrib.auth.models import AbstractBaseUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name="first name")
    last_name = models.CharField(max_length=255, verbose_name="last name")
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=20, verbose_name="phone number", **NULLABLE)
    city = models.CharField(max_length=35, verbose_name="city", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="avatar", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

