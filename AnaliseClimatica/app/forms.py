from django import forms
from .models import *

# inicializando um formulario para os livros
class EstadosForm (forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome', 'pais', 'temperatura', 'clima']
        