from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Sigla, Tipo_componente, Traduzione

# Create your views here.

class SigleView(ListView):
    model = Sigla


class SiglaNewView(CreateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = "/moduli/sigle/"

class SiglaEditView(UpdateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = "/moduli/sigle/"


class SiglaDeleteView(DeleteView):
    """ utilizza in automatico il template : sigla_confirm_delete.html """
    model = Sigla
    success_url = "/moduli/sigle/"
