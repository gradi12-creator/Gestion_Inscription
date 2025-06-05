from django.db import models

# Create your models here.
class Année_scolaire(models.Model):
    libellé=models.CharField(max_length=255)

    def __str__(self):
        return self.libellé
