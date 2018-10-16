from django.forms import ModelForm
from .models import Sigla

class SiglaForm(ModelForm):
    class Meta:
        model = Sigla
        fields = ['sigla', 'descrizione', 'tipo']
