from django.db import models
from django.utils.translation import gettext as _


class Visitor(models.Model):

    STATUS_VISITOR = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada"),
    ]

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

    status = models.CharField(
        max_length=10,
        choices=STATUS_VISITOR,
        default="AGUARDANDO"
    )

    def get_departure_time(self):
        if self.departure_time:
            return self.departure_time
        return "Horário de saida não registrado"

    def get_authorization_time(self):
        if self.authorization_time:
            return self.authorization_time

        return "Visitante aguardando autorização"

    def get_responsible_resident(self):
        if self.responsible_resident:
            return self.responsible_resident

        return "Visitante aguardando autorização"

    def get_vehicle_plate(self):
        if self.vehicle_plate:
            return self.vehicle_plate

        return "Veiculo não registrado"

    def get_cpf(self):
        if self.cpf:
            cpf = self.cpf

            cpf_primeira = cpf[0:3]
            cpf_segunda = cpf[3:6]
            cpf_terceira = cpf[6:9]
            cpf_quarta = cpf[9:]

            return f'{cpf_primeira}.{cpf_segunda}.{cpf_terceira}-{cpf_quarta}'

    class Meta:
        verbose_name = _("Visitante")
        verbose_name_plural = _("Visitantes")

    def __str__(self):
        return self.name
