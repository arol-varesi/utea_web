from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.

class TipoComponente(models.Model):
    """
    Tipologia, o meglio famiglia del componente.
    Oltre al tipo viene anche indicato il prefisso utilizzato (max 3 lettere)
    """
    tipo = models.CharField(max_length = 30)
    prefisso = models.CharField(max_length = 3)

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
    descrizione = CharField(max_length = 30)
    traduzione = models.ManyToManyField(Descrizione, 
                                        through='Traduzioni',
                                        through_fields=('sigla','lingua'),)
    tipo_componente = models.ForeignKey(TipoComponente, on_delete=models.CASCADE)

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name_plural = "sigle"
