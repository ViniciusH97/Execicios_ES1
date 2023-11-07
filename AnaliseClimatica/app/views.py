from django.shortcuts import render
from . models import *

def Consultar(request):
    consultar = {
        'continentes': Continentes.objects.all()
    }
    return render(request, 'continentes/continentes.html', Consultar)


def Adm(request):
    adm = {
        'adm': adm.objects.all()
    }
    return render(request, 'administração/adm.html', Adm)