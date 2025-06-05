from django.db import models
from Gestion_Enseignants.models import Enseignant

# Create your models here.
class Classe(models.Model):
    Libellé=models.CharField(max_length=255)
    Titulaire=models.ForeignKey(Enseignant,on_delete=models.CASCADE)

    def __str__(self):
        return self.Libellé
        