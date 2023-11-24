from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_LENGTH = 30
EMAIL_LENGTH = 254
USERNAME_LENGTH = 150
PHONE_LENGTH = 12
USERS_ROLES = (
    ('admin', 'admin'),
    ('user', 'user'),
)


class User(AbstractUser):
    """Кастомная модель пользователя."""
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email', 'password']
    username = models.CharField(
        max_length=USERNAME_LENGTH,
        unique=True,
        verbose_name='Username',
    )
    role = models.CharField(
        max_length=ROLE_LENGTH,
        choices=USERS_ROLES,
        default='user',
        blank=True
    )
    email = models.EmailField(
        max_length=EMAIL_LENGTH,
        unique=True,
        verbose_name='Email',
        blank=True,
        default='default@ya.ru',
    )
    first_name = models.CharField(
        max_length=USERNAME_LENGTH,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=USERNAME_LENGTH,
        blank=True,
        verbose_name='Фамилия'
    )
    phone = models.CharField(
        max_length=PHONE_LENGTH,
        unique=True,
        verbose_name='Номер телефона'
    )

    @property
    def is_admin(self):
        return self.role == 'admin'

    class Meta:
        ordering = ('id',)
