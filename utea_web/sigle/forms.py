from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Sigla, Trad_sigla

class SiglaForm(ModelForm):
    class Meta:
        model = Sigla
        fields = ['sigla', 'descrizione', 'tipo']

class TraduzioneForm(ModelForm):
    class Meta:
        model = Trad_sigla
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['traduzione'].widget.attrs.update({'class': 'form-control is-valid'})
        self.fields['lingua'].widget.attrs.update({'class': 'form-control'})



TraduzioniFormSet = inlineformset_factory(Sigla, Trad_sigla, form=TraduzioneForm, extra=1)
