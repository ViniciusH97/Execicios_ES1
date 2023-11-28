from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from app.forms import *
from . models import *

def paises(request):
    pais = {
        'pais': pais.objects.all()
    }
    return render(request, 'paises/paises.html', pais)


def adm(request):
    return render(request, 'adm/adm.html')


