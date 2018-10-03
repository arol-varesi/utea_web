from django.shortcuts import render
from django.views.generic import ListView
from .models import Sigla, Tipo_componente, Traduzione

# Create your views here.

class SigleView(ListView):
    model = Sigla
