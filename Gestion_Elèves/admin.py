from django.contrib import admin
from Gestion_Elèves.models import Elève
# Register your models here.

class EleveAdmin(admin.ModelAdmin):
    list_display=['Nom','Postnom','Prénom','Sexe','Date_de_naissance']
    search_fields=['Nom','Postnom','Prénom']
    list_filter=['Sexe','Date_de_naissance']
admin.site.register(Elève,EleveAdmin)
