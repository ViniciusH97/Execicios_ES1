from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('paises/', TemplateView.as_view(template_name='paises/paises.html'), name='paises'),
    path('Administracao/', TemplateView.as_view(template_name='administração/adm.html'), name='Administracao'),
    path('Cidades/', TemplateView.as_view(template_name='cidades/cidades.html'), name='Cidades'),
]