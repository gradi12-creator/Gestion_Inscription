from django.db import models
from Gestion_Classes.models import Classe
from Gestion_Elèves.models import Elève
from Gestion_Années_Scolaires.models import Année_scolaire
# Create your models here.

class Inscription(models.Model):
    Date=models.DateField()
    Elève=models.ForeignKey(Elève, on_delete=models.CASCADE)
    Classe=models.ForeignKey(Classe,on_delete=models.CASCADE)
    Année=models.ForeignKey(Année_scolaire,on_delete=models.CASCADE)