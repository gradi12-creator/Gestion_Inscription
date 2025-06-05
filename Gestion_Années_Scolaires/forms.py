from django import forms
from .models import Année_scolaire

class AnneeForm(forms.ModelForm):
    class Meta:
        model=Année_scolaire
        fields=['libellé']