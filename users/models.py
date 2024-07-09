from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserType(models.Model):
    """
    Модель, представляющая тип пользователя системы
    """

    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    """
    Менеджер для модели User, учитывающий новое поле - phone.
    """

    def _create_user(self, phone, email=None, password=None, **extra_fields):
        if not phone:
            raise ValueError('The given phone must be set')
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Пользователь системы.

    Поля phone и password обязательные, остальные - опциональные
    """

    phone_validator = RegexValidator(
        regex=r'^\+\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phone = models.CharField(unique=True, max_length=16, validators=[phone_validator])
    email = models.EmailField(unique=True, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    patronymic = models.CharField(max_length=150, blank=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
