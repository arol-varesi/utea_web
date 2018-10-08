from django.contrib import admin

from .models import Lingua

# Register your models here.
@admin.register(Lingua)
class LinguaModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'lingua', 'originale')
