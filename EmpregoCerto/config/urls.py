
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('empresas/', empresa ,name='empresas'),
    path('usuarios/', usuario ,name='usuarios'),
    path('vagas/', vaga ,name='vagas'),
    path('candidatos/', candidato ,name='candidatos'),
    path('login/', login ,name='login')
]

