from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    template_name = "moduli/sigla_list_edit.html"


class SiglaNewView(CreateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = reverse_lazy('moduli:sigle-list')

class SiglaEditView(UpdateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = reverse_lazy('moduli:sigle-list')

    def get_context_data(self, **kwargs):
        context = super(SiglaEditView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = TraduzioniFormSet(self.request.POST, instance=self.object)
            context['formset'].full_clean()
        else:
            context['formset'] = TraduzioniFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


        # sigla = self.object
        # TraduzioniFormSet = inlineformset_factory(Sigla, Traduzione, fields=('lingua','traduzione'))
        # #sigla=Sigla.objects.get(pk=self.pk)
        # formset = TraduzioniFormSet(instance=sigla)
        # context['formset'] = formset
        # return context



class SiglaDeleteView(DeleteView):
    """ utilizza in automatico il template : sigla_confirm_delete.html """
    model = Sigla
    success_url = "/moduli/sigle/"
