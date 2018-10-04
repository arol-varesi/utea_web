from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Sigla, Tipo_componente, Traduzione

# Create your views here.

class SigleView(ListView):
    model = Sigla


class SiglaAddView(CreateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = 'sigle'
