from django.contrib import admin
from .models import *
from core.models import Lingua as core_lingua

# Personalizzazione dell'applicazione admin

class SiglaInModuloInLine(admin.TabularInline):
    model = SiglaInModulo
    extra = 0


@admin.register(Modulo)
class ModuloModelAdmin(admin.ModelAdmin):
    list_display = ('id','descrizione','tipo','opzione')
    inlines = [
        SiglaInModuloInLine,
    ]

admin.site.register(TipoModulo)
