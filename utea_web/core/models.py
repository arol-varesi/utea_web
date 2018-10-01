from django.db import models

# Create your models here.


class Lingua(models.Model):
    """
    Lista delle lingue utilizzate per le traduzioni.
    lingua    : è la lingua in italiano (es. inglese, tedesco)
    originale : è la lingua in originale (es: english, deutsche)
    sigla     : è la sigla internazionale (es. EN, DE)
    """
    lingua = models.CharField(max_length = 20)
    originale = models.CharField(max_length = 20)
    sigla = models.CharField(max_length = 2)

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name = "lingua"
        verbose_name_plural = "lingue"
