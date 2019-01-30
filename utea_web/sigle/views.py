from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from extra_views import InlineFormSet, UpdateWithInlinesView, CreateWithInlinesView
from core.models import Lingua
from .models import Sigla, Tipo_componente, Trad_sigla
from .forms import SiglaForm, TraduzioniFormSet
import sys


def sigla_new_test(request):
    # user = User.objects.first() # TODO: get the current logged in user
    if request.method == 'POST':
        form = SiglaForm(request.POST)
        formset = TraduzioniFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            sigla = form.save(commit=False)
            sigla.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.sigla=sigla
                instance.save()
            return redirect('sigle:sigle-test')
    else:
        form = SiglaForm()
        formset = TraduzioniFormSet()
    return render(request, 'sigle/new_sigla.html', {
        'form' : form,
        'formset' : formset
    })

def sigla_edit_test(request, pk):
    sigla = Sigla.objects.get(pk=pk)
    # user = User.objects.first() # TODO: get the current logged in user
    if request.method == 'POST':
        print ("POST")
        form = SiglaForm(request.POST, instance= sigla)
        formset = TraduzioniFormSet(request.POST, request.FILES, instance = sigla)
        if form.is_valid() and formset.is_valid():
            print ("Is VALID")
            sigla = form.save(commit=False)
            sigla.save()
            traduzioni = formset.save(commit=False)
            for trad in traduzioni:
                print("--------------")
                print (trad.lingua)
                trad.sigla=sigla
                trad.save()
            return redirect('sigle:sigle-test')
    else:
        form = SiglaForm(instance = sigla)
        formset = TraduzioniFormSet(instance = sigla)
    return render(request, 'sigle/new_sigla.html', {
        'form' : form,
        'formset' : formset
    })



class SigleView(ListView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = reverse_lazy('sigle:sigle-list')

class SigleViewTest(ListView):
    model = Sigla
    template_name = 'sigle/sigle_test2.html'
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = reverse_lazy('sigle:sigle-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lingua'] = Lingua.objects.all()
        return context

class TraduzioniInLine(InlineFormSet):
    model = Trad_sigla
    factory_kwargs = {'extra': 1}
    fields = '__all__'

class SiglaNewView(CreateWithInlinesView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    inlines = [TraduzioniInLine, ]
    success_url = reverse_lazy('sigle:sigle-list')

class SiglaNewViewTest(CreateView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    success_url = reverse_lazy('sigle:sigle-test')

    def get(self, request, *args, **kwargs):
        """ Handles GET requests. """
        self.object = Sigla()
        # Get latest revision

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        traduzioni_form = TraduzioniFormSet

        return self.render_to_response(
            self.get_context_data(form=form,
                                  formset=traduzioni_form))



class SiglaEditView(UpdateWithInlinesView):
    model = Sigla
    fields = ['sigla', 'descrizione', 'tipo']
    inlines = [TraduzioniInLine, ]
    #success_url = reverse_lazy('sigle:sigle-list', pk)
    #success_url = reverse_lazy('sigle:sigle-list')


class SiglaDeleteView(DeleteView):
    """ utilizza in automatico il template : sigla_confirm_delete.html """
    model = Sigla
    success_url = "/sigle/"
