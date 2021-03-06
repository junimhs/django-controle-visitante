from django.db import models
from django.utils.translation import gettext as _


class Visitor(models.Model):
    name = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )
    birth_date = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False
    )
    number_home = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada"
    )
    vehicle_plate = models.CharField(
        verbose_name="Placa do veículo",
        max_length=7,
        null=True,
        blank=True
    )
    arrival_time = models.DateTimeField(
        verbose_name="Horário de chegada na portaria",
        auto_now_add=True
    )
    departure_time = models.DateTimeField(
        verbose_name="Horário de saida do condominio",
        auto_now=False,
        blank=True,
        null=True
    )
    authorization_time = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True
    )
    responsible_resident = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
        null=True
    )
    registered_by = models.ForeignKey(
        'gatekeepers.Gatekeeper',
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _("Visitante")
        verbose_name_plural = _("Visitantes")

    def __str__(self):
        return self.name
