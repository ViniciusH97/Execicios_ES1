
from django.shortcuts import render
from . models import *

def empresa(request):
    empresas = {
        'empresas': empresa.objects.all()
    }
    return render(request, 'Empresa/empresas.html', empresas)

def usuario(request):
    usuarios = {
        'usuario': usuario.objects.all()
    }
    return render (request, 'Usuarios/usuarios.html', usuarios)

def vaga(request):
    vagas = {
        'vaga': vaga.objects.all()
    }
    return render (request, 'Vagas/vagas.html', vagas)

def candidato(request):
    candidatos = {
        'candidato': candidato.objects.all()
    }
    return render (request, 'Candidatos/candidatos.html', candidatos)

def login(request):
    logins = {
        'login': login.objects.all()
    }
    return render (request, 'login/login.html', logins)

def index(request):
    return render (request, 'index.html')