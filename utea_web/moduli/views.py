# moduli/views.py
from django.views.generic import ListView, DetailView, CreateView
from .models import Sigla, Tipo_componente, Traduzione
from core.models import Lingua

class SiglaList(ListView):
    model = Sigla

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lingua'] = Lingua.objects.all()
        return context



class SiglaAddView(CreateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = 'sigle'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context


class SiglaDetail(DetailView):
    """

    """
    model = Sigla

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lingua'] = Lingua.objects.all()
        return context
