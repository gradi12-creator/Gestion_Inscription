from django.shortcuts import render,redirect
from Gestion_Inscriptions.models import Inscription
from Gestion_Inscriptions.forms import InscriptionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from .forms import LoginForm

@login_required

def inscription (request):
    context={}
    context['inscriptions']=Inscription.objects.all()
    return render (request, template_name='inscription.html',context=context)

def ajouterInscription(request):
    if request.method=='POST':
        form=InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('inscription')
    else:
        form=InscriptionForm()
    return render (request, 'ajouterInscription.html',{'form':form})

def login_view(request):
    form=LoginForm(request.POST or None)
    if request.method=='POST':
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']
              user=authenticate(request,username=username,password=password)
              if user is not None:
                  login(request, user)
                  return redirect('inscription')
              else:
                  form.add_error(None, "Nom d'utilisateur ou Mot de passe incorrect")
    return render (request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

    
