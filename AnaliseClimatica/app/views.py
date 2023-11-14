from django.shortcuts import render
from . models import *

def paises(request):
    pais = {
        'pais': pais.objects.all()
    }
    return render(request, 'paises/paises.html', pais)


def Administracao(request):
    adm = {
        'adm': adm.objects.all()
    }
    return render(request, 'administração/adm.html', adm)