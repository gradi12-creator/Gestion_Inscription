"""
URL configuration for InscriptionScolaire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from Gestion_Inscriptions.views import inscription
from Gestion_Années_Scolaires.views import Annee
from Gestion_Classes.views import classe
from Gestion_Elèves.views import Eleve
from Gestion_Enseignants.views import enseignant
from Gestion_Années_Scolaires.views import ajouterAnnee
from Gestion_Classes.views import ajouterClasse
from Gestion_Elèves.views import ajouterEleve
from Gestion_Enseignants.views import ajouterEnseignant
from Gestion_Inscriptions.views import ajouterInscription
from Gestion_Inscriptions.views import login_view
from Gestion_Inscriptions.views import logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name='login'),
    path('inscription',inscription,name='inscription'),
    path('Annee',Annee,name='Années'),
    path('classe',classe, name='classe'),
    path('eleve',Eleve, name='eleve'),
    path('enseignant',enseignant, name='enseignant'),
    path('ajout_Annee',ajouterAnnee, name='AjouterAnnee'),
    path('ajout_Classe',ajouterClasse,name='AjouterClasse'),
    path('ajout_Eleve',ajouterEleve,name='AjouterEleve'),
    path('ajout_Enseignant',ajouterEnseignant,name='AjouterEnseignant'),
    path('ajout_Inscription',ajouterInscription,name='AjouterInscription'),
    path('logout/',logout_view,name='logout'),
    #path('login/',login_view,name='login'),
    #path('modifier_annee/<int:id>/',modifier,name='ModifierAnnee'),
  

  
   
    
   
]
