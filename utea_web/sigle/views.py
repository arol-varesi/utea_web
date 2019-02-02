from django.contrib.auth.models import User
# from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from extra_views import InlineFormSet, UpdateWithInlinesView, CreateWithInlinesView
from core.models import Lingua
from .models import Sigla, Tipo_componente, Trad_sigla
from .forms import SiglaForm, TraduzioniFormSet, TipoComponenteForm
from django.views.decorators.csrf import csrf_exempt
import json


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
    form_class = SiglaForm
    inlines = [TraduzioniInLine, ]
    success_url = reverse_lazy('sigle:sigle-list')


class SiglaEditView(UpdateWithInlinesView):
    model = Sigla
    form_class = SiglaForm
    inlines = [TraduzioniInLine, ]
    #success_url = reverse_lazy('sigle:sigle-list', pk)
    #success_url = reverse_lazy('sigle:sigle-list')

class SiglaDeleteView(DeleteView):
    """ utilizza in automatico il template : sigla_confirm_delete.html """
    model = Sigla
    success_url = "/sigle/"


def TipoCreatePopup(request):
    form = TipoComponenteForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_tipo");</script>' % (instance.pk, instance))
    return render(request,'sigle/tipo_form.html', {"form" : form})


@csrf_exempt
def get_tipo_id(request):
    if request.is_ajax():
        tipo_tipo = request.GET['tipo_tipo']
        tipo_id = Tipo_componente.objects.get(tipo = tipo_tipo).id
        data = {'tipo_id':tipo_id,}
        return HttpResponse(json.dumps(data), content_type = 'application/json')
    return HttpResponse("/")
