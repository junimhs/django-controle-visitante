from django.db import models
from django.utils.translation import gettext as _


class Gatekeeper(models.Model):
    user = models.OneToOneField(
        'users.User',
        verbose_name='usuario',
        on_delete=models.PROTECT
    )
    name = models.CharField(
        verbose_name='nome completo',
        max_length=194
    )
    cpf = models.CharField(
        verbose_name='CPF',
        max_length=11
    )
    phone = models.CharField(
        verbose_name='telefone',
        max_length=11
    )
    birth_date = models.DateField(
        verbose_name='data de nascimento',
        auto_now=False,
        auto_now_add=False
    )

    class Meta:
        verbose_name = _('Porteiro')
        verbose_name_plural = _('Porteiros')

    def __str__(self):
        return self.name
