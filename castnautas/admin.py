from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from ckeditor.widgets import CKEditorWidget

# Register your models here.

from .models import *

class PostagemForm(ModelForm):
    class Meta:
        widgets = {
            'texto': CKEditorWidget()
        }


class PostagemAdmin(admin.ModelAdmin):
    form = PostagemForm
    fieldsets = [
        (None, {
            'fields': ('titulo', 'resumo','texto','imagem_carrossel', 'imagem_pequena','imagem_grande','url_comentarios','data','categorias')
        }),

    ]

    list_display = ('titulo','dia' ,'resumo','categorias_list')


    search_fields = ['id','titulo','data']
    list_filter =('categorias','data')

    def categorias_list(self, obj):

        return "/".join([p.nome for p in obj.categorias.all()])


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display_links =[ 'id']
    list_display = ['id','nome']
    list_editable = ['nome' ]
    list_filter = ['postagem']

admin.site.register(Postagem,PostagemAdmin)
admin.site.register(Categoria,CategoriaAdmin)