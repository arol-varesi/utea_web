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

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name_plural = "sigle"


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



class Modulo(models.Model):
    """
    Per modulo si intende un gruppo funzionale della macchina,
    esempi di moduli sono:
    . Orientatore centrifugo a selezione interna (doppio formato)
    . Canale tappi con doppio Sensore
    . Pressostato
    E' formato dai seguenti campi:
    id = identificativo es: CENT_SELINT_2FR
    descrizione = descrizione estesa del modulo
    tipo = punta al tipo di modulo : es: Orientatore
    opzione = se True indica che si tratta di un'opzione del tipo di modulo
    """
    id_modulo = models.CharField(max_length = 20)
    descrizione = models.CharField(max_length = 60)
    tipo = models.ForeignKey('TipoModulo', on_delete=models.CASCADE)
    # opzione = models.BooleanField()

    def __str__(self):
        return f"{self.id_modulo}: {self.descrizione}"

    class Meta:
        verbose_name_plural = "moduli"


class TipoModulo(models.Model):
    tipo = models.CharField(max_length = 20)


    class Meta:
        verbose_name = "tipo di modulo"
        verbose_name_plural = "tipi di modulo"
