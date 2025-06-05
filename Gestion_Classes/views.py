from django.shortcuts import render,redirect,get_object_or_404
from Gestion_Classes.models import Classe
from Gestion_Classes.forms import ClasseForm

# Create your views here.
def classe (request):
    context={}
    context['classes']=Classe.objects.all()
    return render (request, template_name='classe.html',context=context)

def ajouterClasse(request):
    if request.method=='POST':
        form=ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('classe')
    else:
        form=ClasseForm()
    return render (request, 'ajouterClasse.html',{'form':form})