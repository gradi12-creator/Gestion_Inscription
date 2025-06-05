from django import forms
from .models import Enseignant

class EnseignantForm(forms.ModelForm):
    class Meta:
        model=Enseignant
        fields=['Nom','Postnom','Prénom','Sexe','Niveau_Etudes','Date_de_naissance']
        Date_de_naissance=forms.DateField(widget=forms.DateInput(attrs={'type':'date-local'}))

        def __init__(self):
            super(EnseignantForm,self).__init__()
            self.fields['Date_de_naissance']