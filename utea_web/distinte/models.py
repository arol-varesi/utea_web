from django.db import models



class DBMag(models.Model):
    """
    Magazzino Arol . Potrebbe essere sostituito da un database esterno
    """
    arol_code = models.CharField(max_length = 12)
    commercial_code = models.CharField(max_length = 30)
    description = models.CharField(max_length = 50)
    manufacturer = models.ForeignKey("Marca", on_delete=models.CASCADE)
    supplementary_description = models.TextField()

    def __str__(self):
        return self.arol_code

    class Meta:
        verbose_name = "componente"
        verbose_name_plural = "componenti"


class Macro(models.Model):
    """
    La macro consiste di una mini distinta di componenti elettrici abbinati
    ad una data funzione (Sigla) che vengono forniti in blocco.
    Esempio tipico sono : fotocellula + cavetto + catarinfrangente
    """
    macro = models.CharField(max_length = 10)
    famiglia = models.ForeignKey("Famiglia", on_delete=models.CASCADE)
    marca = models.ForeignKey("Marca", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    componenti = models.ManyToManyField("DBMag")


class Famiglia(models.Model):
    pass

class Marca(models.Model):
    pass

class Tag(models.Model):
    pass