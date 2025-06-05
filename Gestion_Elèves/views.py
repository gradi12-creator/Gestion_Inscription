from django.shortcuts import render,redirect,get_object_or_404
from Gestion_Elèves.models import Elève
from Gestion_Elèves.forms import EleveForm

def Eleve (request):
    context={}
    context['eleves']=Elève.objects.all()
    return render (request, template_name='eleve.html',context=context)

def ajouterEleve(request):
    if request.method=='POST':
        form=EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('eleve')
    else:
        form=EleveForm()
    return render (request, 'ajouterEleve.html',{'form':form})
