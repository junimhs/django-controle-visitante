from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='e-mail do usuário',
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        db_table = 'auth.user'

    def __str__(self):
        return self.email

