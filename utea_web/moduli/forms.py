from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Sigla

class SiglaForm(ModelForm):
    class Meta:
        model = Sigla
        fields = ['sigla', 'descrizione', 'tipo']


class ExampleForm(ModelForm):
    class Meta:
        model = Sigla
        fields = '__all__'

class NewSigla(ModelForm):
    class Meta:
        model = Sigla
        fields = '__all__'
