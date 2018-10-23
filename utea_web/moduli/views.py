from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Sigla, Tipo_componente, Traduzione
from .forms import SiglaForm, ExampleForm
from core.models import Lingua

# Create your views here.

class SigleView(ListView):
    model = Sigla

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit_form'] = SiglaForm
        return context


class Sigle2View(ListView):
    model = Sigla
    template_name = "moduli/sigle_test2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lingua'] = Lingua.objects.all()
        return context

class SigleViewEdit(ListView):
    model = Sigla
    template_name = "moduli/sigla_list_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiglaNewView(CreateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = "/moduli/sigle/"
#    success_url = reverse('moduli:sigle')

class SiglaEditView(UpdateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = "/moduli/sigle/"

class ExampleEditView(UpdateView):
    model = Sigla
    form_class = ExampleForm
    template_name = 'moduli/example_form.html'
    success_url = "/moduli/sigle/"


class SiglaDeleteView(DeleteView):
    """ utilizza in automatico il template : sigla_confirm_delete.html """
    model = Sigla
    success_url = "/moduli/sigle/"
