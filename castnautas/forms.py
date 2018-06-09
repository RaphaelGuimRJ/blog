from django.forms import *
from .models import *
from django import forms

from castnautas.models import Postagem


class BuscaForm(ModelForm):

    class Meta:
        model = Postagem
        fields = ['categorias']

        widgets = {
            'categorias': forms.TextInput(),
        }
