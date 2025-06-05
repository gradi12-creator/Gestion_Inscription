from django.db import models

# Create your models here.
class Enseignant(models.Model):
    Nom=models.CharField(max_length=255,null=False)
    Postnom=models.CharField(max_length=255,null=True)
    Prénom=models.CharField(max_length=55,null=True)
    Sexe=models.CharField(max_length=1, choices=[('M','Masculin'),('F','Féminin')])
    NVE=[('Diplômé Etat','Diplômé Etat'),('Gradué','Gradué'),('Licencié','Licencié'),('Autre','Autre')]
    Niveau_Etudes=models.CharField(max_length=200, choices=NVE)
    Date_de_naissance=models.DateField()

    def __str__(self):
        return self.Nom
