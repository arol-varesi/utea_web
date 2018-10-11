from django.contrib import admin
from .models import Tipo_componente, Sigla, Traduzione, Modulo, TipoModulo
from core.models import Lingua as core_lingua

# Personalizzazione dell'applicazione admin

class TraduzioneInLine(admin.TabularInline):
    model = Traduzione
    extra = 0

@admin.register(Sigla)
class SiglaModelAdmin(admin.ModelAdmin):
    list_filter = ('sigla', 'tipo', )
    list_display = ('sigla', 'descrizione', 'tipo',)
    inlines = [
        TraduzioneInLine,
    ]

@admin.register(Traduzione)
class TraduzioneModelAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'traduzione')


# Register your models here.
admin.site.register(Tipo_componente)

admin.site.register(Modulo)
admin.site.register(TipoModulo)
