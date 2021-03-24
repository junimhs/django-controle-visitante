from django import forms
from visitors.models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'cpf', 'birth_date', 'number_home', 'vehicle_plate']
        error_messages = {
            "name": {
                "required": "O nome completo do visitante é obrigatorio para o registro"
            },
            "cpf": {
                "required": "O CPF do visitante é obrigatorio para o registro"
            },
            "birth_date": {
                "required": "A data de nascimento do visitante é obrigatorio para o registro",
                "invalid": 'Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)'
            },
            "number_home": {
                "required": "Informe o numero da casa á ser visitada"
            }
        }
