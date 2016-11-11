from django.forms import ModelForm
from .models import infoGeneral


class infoGeneralForm(ModelForm):
    class Meta:
        model = infoGeneral
        fields = ["nombre", "email","semestre","edad", "carrera", "telefono"]