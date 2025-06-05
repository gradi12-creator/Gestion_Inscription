from django.db import models

# Create your models here.
class Elève(models.Model):
    Nom=models.CharField(max_length=255, null=False)
    Postnom=models.CharField(max_length=255,null=True)
    Prénom=models.CharField(max_length=255,null=True)
    Sexe=models.CharField(max_length=1, choices=[('M','Masculin'),('F','Féminin')])
    Date_de_naissance=models.DateField()

    def __str__(self):
        return self.Nom
    