from django.contrib import admin
from Gestion_Inscriptions.models import Inscription
# Register your models here.

class InscriptionAdmin(admin.ModelAdmin):
    list_display=['Date','Elève','Classe','Année']
    search_fields=['Elève']
    list_filter=['Date','Classe','Année']
admin.site.register(Inscription,InscriptionAdmin)
