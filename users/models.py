from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    """ this is class of selection the role """

    USER = 'user', _('user'),
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name="first name")
    last_name = models.CharField(max_length=255, verbose_name="last name")
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=20, verbose_name="phone number", **NULLABLE)
    city = models.CharField(max_length=35, verbose_name="city", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="avatar", **NULLABLE)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

