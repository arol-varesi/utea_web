from django.contrib import admin
from .models import Tipo_componente, Sigla, Traduzione
from core.models import Lingua as core_lingua

# Personalizzazione dell'applicazione admin

class TraduzioneInLine(admin.TabularInline):
    model = Traduzione
    extra = 0

@admin.register(Sigla)
class SiglaModelAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'descrizione')
    inlines = [
        TraduzioneInLine,
    ]

@admin.register(Traduzione)
class TraduzioneModelAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'traduzione')


# Register your models here.
admin.site.register(Tipo_componente)
admin.site.register(core_lingua)
