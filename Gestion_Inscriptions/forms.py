from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model=Inscription
        fields=['Date','Elève','Classe','Année']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)