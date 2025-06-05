from django.db import models

# Create your models here.
class Frais(models.Model):
    Montant=models.DecimalField(decimal_places=2, max_digits=10)
    Motif=models.CharField(max_length=100, choices=[('Frais scolaire','Frais scolaire'),('Inscription','Inscription'),('Autre','Autre')])
    Date=models.DateTimeField()