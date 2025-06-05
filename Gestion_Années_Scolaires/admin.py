from django.contrib import admin
from Gestion_Années_Scolaires.models import Année_scolaire
# Register your models here.

class Annee_scolaireAdmin(admin.ModelAdmin):
    list_display=['libellé']
admin.site.register(Année_scolaire,Annee_scolaireAdmin)