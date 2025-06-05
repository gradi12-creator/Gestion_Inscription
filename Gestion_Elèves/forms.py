from django import forms
from .models import Elève

class EleveForm(forms.ModelForm):
    class Meta:
        model=Elève
        fields=['Nom','Postnom','Prénom','Sexe','Date_de_naissance']