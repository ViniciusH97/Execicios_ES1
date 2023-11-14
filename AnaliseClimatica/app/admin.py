from django.contrib import admin
from app.models import *
from app.forms import *

admin.site.register(Estado)
admin.site.register(Clima)
admin.site.register(Continentes)


class EstadoInline(admin.TabularInline):
    model = Estado
    extra = 1
    form = EstadosForm
    
class PaisAdmin(admin.ModelAdmin):
    inlines = [EstadoInline]  
    
admin.site.register(Pais, PaisAdmin)
