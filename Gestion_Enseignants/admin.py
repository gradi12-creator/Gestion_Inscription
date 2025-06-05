from django.contrib import admin
from Gestion_Enseignants.models import Enseignant
# Register your models here.

class EnseignantAdmin(admin.ModelAdmin):
    list_display=['Nom','Postnom','Prénom','Sexe','Niveau_Etudes','Date_de_naissance']
    search_fields=['Nom','Postnom','Prénom']
    list_filter=['Sexe','Niveau_Etudes']
admin.site.register(Enseignant,EnseignantAdmin)