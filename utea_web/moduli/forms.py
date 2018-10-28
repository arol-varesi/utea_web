from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Sigla, Traduzione

class SiglaForm(ModelForm):
    class Meta:
        model = Sigla
        fields = ['sigla', 'descrizione', 'tipo']

TraduzioniFormSet = inlineformset_factory(Sigla, Traduzione, extra=1, fields=('lingua','traduzione'))
