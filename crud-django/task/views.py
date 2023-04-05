from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def home(request):
    titulo = "Home"
    return render(request, 'home.html', {
                'title': titulo
            })


def registro_user(request):
    if request.method == "GET":
            titulo = "Registrate"
            return render(request, 'registro.html', {
                'title': titulo,
                'form': UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError: 
                titulo = "Error"
                return render(request, 'registro.html', {
                    'title': titulo,
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
            
        return render(request, 'registro.html', {
                        'title': 'Error',
                        'form': UserCreationForm,
                        'error': 'No coinciden las contraseñas'
                    })

def show_tasks(request):
    titulo = "Tareas"
    return render(request, 'tasks.html', {
                    'title': titulo,
                })

def inicio_sesion(request):
    title = "Inicia Sesión"
    if request.method == "GET":     
        return render(request, 'login.html', {
                        'title': title,
                        'form': AuthenticationForm
                    })
    
    if request.method == "POST":
         
         return render(request, 'login.html', {
                        'title': title,
                        'form': AuthenticationForm
                    })

def cerrar_sesion(request):
     logout(request)
     return redirect('home')