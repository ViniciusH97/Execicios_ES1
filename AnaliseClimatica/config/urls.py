from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('adm', TemplateView.as_view(template_name='adm/adm.html'), name='adm'),
    path('index', TemplateView.as_view(template_name='index.html'), name='index'),
]   