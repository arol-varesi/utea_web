from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from extra_views import InlineFormSet, UpdateWithInlinesView, CreateWithInlinesView
from core.models import Lingua
from .models import Sigla, Tipo_componente, Traduzione
from .forms import SiglaForm, TraduzioniFormSet

def new_sigla(request):
    user = User.objects.first() # TODO: get the current logged in user
    if request.method == 'POST':
        form = SiglaForm(request.POST)
        if form.is_valid():
            sigla = form.save(commit=False)
            sigla.save()
            return redirect('moduli:sigle')
    else:
        form = SiglaForm()
    return render(request, 'moduli/new_sigla.html', {'form' : form })


class SigleView(ListView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = reverse_lazy('moduli:sigle-list')

class TraduzioniInLine(InlineFormSet):
    model = Traduzione
    factory_kwargs = {'extra': 1}
    fields = '__all__'

class SiglaNewView(CreateWithInlinesView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    inlines = [TraduzioniInLine, ]
    success_url = reverse_lazy('moduli:sigle-list')


class SiglaEditView(UpdateWithInlinesView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    inlines = [TraduzioniInLine, ]
    success_url = reverse_lazy('moduli:sigle-list')


class SiglaDeleteView(DeleteView):
    """ utilizza in automatico il template : sigla_confirm_delete.html """
    model = Sigla
    success_url = "/moduli/sigle/"
