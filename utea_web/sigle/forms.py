from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Sigla, Trad_sigla

class SiglaForm(ModelForm):
    class Meta:
        model = Sigla
        fields = ['sigla', 'descrizione', 'tipo']

TraduzioniFormSet = inlineformset_factory(Sigla, Trad_sigla, extra=1, fields=('lingua','traduzione'))
