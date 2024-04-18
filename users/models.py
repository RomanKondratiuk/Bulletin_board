from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        """
        Retrieve a user by their email (natural key).
        """
        return self.get(email=email)


class UserRoles(models.TextChoices):
    """ this is class of selection the role """

    USER = 'user', _('user'),
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=255, verbose_name="first name")
    last_name = models.CharField(max_length=255, verbose_name="last name")
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=20, verbose_name="phone number", **NULLABLE)
    city = models.CharField(max_length=35, verbose_name="city", default="")
    avatar = models.ImageField(upload_to="users/", verbose_name="avatar", **NULLABLE)
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.USER)
    is_staff = models.BooleanField(default=False, verbose_name="staff status")
    is_superuser = models.BooleanField(default=False, verbose_name="superuser status")
    is_active = models.BooleanField(default=True, verbose_name="Active")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
