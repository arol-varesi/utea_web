from django.contrib import admin
from .models import Tipo_componente, Sigla, Traduzione
from core.models import Lingua as core_lingua

# Personalizzazione dell'applicazione admin
class SiglaModelAdmin(admin.ModelAdmin):
    model = Sigla
    list_display = ['sigla', 'tipo', 'descrizione']
    search_fields = ['sigla', 'descrizione']



# Register your models here.
admin.site.register(Tipo_componente)
admin.site.register(Sigla, SiglaModelAdmin)
admin.site.register(Traduzione)
admin.site.register(core_lingua)
