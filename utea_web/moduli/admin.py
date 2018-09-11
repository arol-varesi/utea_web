from django.contrib import admin
from .models import TipoComponente, Sigla

# Personalizzazione dell'applicazione admin
class SiglaModelAdmin(admin.ModelAdmin):
    model = Sigla
    list_display = ['sigla', 'tipo_componente', 'descrizione']
    search_fields = ['sigla', 'descrizione']



# Register your models here.
admin.site.register(TipoComponente)
admin.site.register(Sigla, SiglaModelAdmin)
