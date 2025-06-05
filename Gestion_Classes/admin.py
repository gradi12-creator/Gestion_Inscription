from django.contrib import admin
from Gestion_Classes.models import Classe
# Register your models here.

class ClasseAdmin(admin.ModelAdmin):
    list_display=['Libellé','Titulaire']
admin.site.register(Classe,ClasseAdmin)