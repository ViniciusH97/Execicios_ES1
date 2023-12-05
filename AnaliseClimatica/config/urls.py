from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app import views
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('adm', TemplateView.as_view(template_name='adm/adm.html'), name='adm'),
    path('index', TemplateView.as_view(template_name='index.html'), name='index'),
    path('causa', TemplateView.as_view(template_name='causa/consultar_causa.html'), name='causa'),
    path('buscar_causas', views.buscar_causas, name='buscar_causas'),
    path('estado/', views.mostrar_dados, name='estado'),
    path('index', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', views.mostrar_dados, name='index'),

]   
