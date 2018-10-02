from django.db import models

# Create your models here.


class Lingua(models.Model):
    """
    Lista delle lingue utilizzate per le traduzioni.
    lingua    : è la lingua in italiano (es. inglese, tedesco)
    originale : è la lingua in originale (es: english, deutsche)
    sigla     : è la sigla internazionale (es. EN, DE)
    """
    id = models.CharField(max_length = 2, primary_key = True)
    lingua = models.CharField(max_length = 20)
    originale = models.CharField(max_length = 20)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "lingua"
        verbose_name_plural = "lingue"
