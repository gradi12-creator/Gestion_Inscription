from django.shortcuts import render,redirect,get_object_or_404
from Gestion_Années_Scolaires.models import Année_scolaire
from Gestion_Années_Scolaires.forms import AnneeForm

from django.contrib.auth import logout
# Create your views here.
def Annee (request):
    context={}
    context['années']=Année_scolaire.objects.all()
    return render (request, template_name='annee.html',context=context)

def ajouterAnnee(request):
    if request.method=='POST':
        form=AnneeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Années')
    else:
        form=AnneeForm()
    return render (request, 'ajouterAnnee.html',{'form':form})


#def modifier(request, pk):
    #Année_scolaire=get_object_or_404(Année_scolaire, id=id)
    #if request.method=='POST':
        #form=AnneeForm(request.POST, instance=Année_scolaire)
        #if form.is_valid():
            #form.save()
            #return redirect ('Années')
    #else:
        #form=AnneeForm(instance=Année_scolaire)
    #return render (request, 'modifier.html',{'form':form})

