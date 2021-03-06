from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
from core.models import Lingua

# Create your models here.

class Tipo_componente(models.Model):
    """
    Tipologia, o meglio famiglia del componente.
    Oltre al tipo viene anche indicato il prefisso utilizzato (max 3 lettere)
    """
    tipo = models.CharField(max_length = 30)
    prefisso = models.CharField(max_length = 3, unique = True)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "tipologia di componente"
        verbose_name_plural = "tipologie di componenti"



class Sigla(models.Model):
    """
    Contiene la lista delle sigle dei componenti
        (es. B1, SQ6, M2 ...)
    Ad ogni sigla è abbinata la descrizione funzionale
        (es. "Mancanza capsule", "Limite minimo altezza", "Rotazione Teste")
    Ad ogni sigla è abbinato una tipologia di componente (ForeignKey)
        (es. "Fotocellula", "Sensore di prossimità", "Motore")
    """
    sigla = models.CharField(max_length = 5)
    descrizione = models.CharField(max_length = 60)
    tipo = models.ForeignKey(Tipo_componente, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "sigle"
        ordering = ["sigla"]

    def __str__(self):
        return self.sigla

    def get_traduzione(self, lingua):
        return Traduzione.objects.get(lingua=lingua , sigla=self.pk)


class Traduzione(models.Model):
#    """
#    Tabella delle traduzioni delle descrizioni delle sigle
#    """
    sigla = models.ForeignKey('Sigla', on_delete=models.CASCADE)
    lingua = models.ForeignKey(Lingua, on_delete=models.CASCADE)
    traduzione = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.lingua}: {self.traduzione}"

    class Meta:
        verbose_name_plural = "traduzioni"
        unique_together = ("sigla", "lingua")
