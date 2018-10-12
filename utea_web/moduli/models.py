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
    id = models.CharField(max_length = 20, primary_key = True)
    descrizione = models.CharField(max_length = 60)
    tipo = models.ForeignKey('TipoModulo', on_delete=models.CASCADE)
    opzione = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name_plural = "moduli"


class TipoModulo(models.Model):
    """
    Il tipo di modulo serve per categorizzare in vari moduli in modo
    che siano facilmente ricercabili nel momento dell'utilizzo.
    """
    tipo = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.tipo}"

    class Meta:
        verbose_name = "tipo di modulo"
        verbose_name_plural = "tipi di modulo"

class SiglaInModulo(models.Model):
    """
    Contiene la lista delle sigle funzionali che compongono il modulo.
    Per ogni sigla oltre al link alla tabella sigla viene abbinato
    anche una Stringa utilizzata per poter personalizzare la sigla
    ad esempio la B1 potrebbe essere indicata come B1A.
    Esempio "B1{0}"  "B1{1}" supponendo di passare alla configurazione
    il seguente parametro 'suffisso' : ('C' , 'D') si ottengono le seguenti due
    sigle : B1C e B1D
    """
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    sigla = models.ForeignKey(Sigla, on_delete=models.CASCADE)
    etichetta = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.sigla} : {self.sigla.descrizione}"
