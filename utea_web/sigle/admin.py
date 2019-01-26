from django.contrib import admin
from .models import *

# Personalizzazione dell'applicazione admin

class TraduzioneInLine(admin.TabularInline):
    model = Trad_sigla
    extra = 0

@admin.register(Sigla)
class SiglaModelAdmin(admin.ModelAdmin):
    list_filter = ('sigla', 'tipo', )
    list_display = ('sigla', 'descrizione', 'tipo',)
    inlines = [
        TraduzioneInLine,
    ]

@admin.register(Trad_sigla)
class TraduzioneModelAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'traduzione')

admin.site.register(Tipo_componente)
