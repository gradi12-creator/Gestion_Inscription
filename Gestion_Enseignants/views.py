from django.shortcuts import render,redirect,get_object_or_404
from Gestion_Enseignants.models import Enseignant
from Gestion_Enseignants.forms import EnseignantForm
# Create your views here.
def enseignant (request):
    context={}
    context['enseignants']=Enseignant.objects.all()
    return render (request, template_name='enseignant.html',context=context)

def ajouterEnseignant(request):
    if request.method=='POST':
        form=EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('enseignant')
    else:
        form=EnseignantForm()
    return render (request, 'ajouterEnseignant.html',{'form':form})