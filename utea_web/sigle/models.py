
from django.urls import reverse
from django.db import models
from core.models import Lingua

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
    sigla = models.CharField(max_length = 5, help_text="Lunghezza massima 5 caratteri")
    descrizione = models.CharField(max_length = 60, help_text="Lunghezza massima 60 caratteri")
    tipo = models.ForeignKey(Tipo_componente, on_delete=models.CASCADE, help_text="Seleziona da lista")

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name_plural = "sigle"

    def get_absolute_url(self):
        return reverse('sigle:sigla-edit', kwargs={'pk': self.pk})


class Trad_sigla(models.Model):
#    """
#    Tabella delle traduzioni delle descrizioni delle sigle
#    """
    sigla = models.ForeignKey('Sigla', on_delete=models.CASCADE)
    lingua = models.ForeignKey(Lingua, on_delete=models.CASCADE)
    traduzione = models.CharField(max_length = 60)

    def __str__(self):
        return f"{self.lingua}: {self.traduzione}"

    class Meta:
        verbose_name = "traduzione sigla"
        verbose_name_plural = "traduzioni sigle"
        unique_together = ("sigla", "lingua")
