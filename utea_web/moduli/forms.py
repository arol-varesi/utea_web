from django.forms import ModelForm

class SiglaForm(ModelForm):
    class Meta:
        model = Sigla
        fields = ['sigla', 'descrizione', 'tipo']
