from django.db import models
from django.db.models.functions import Substr
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    titulo = models.CharField(max_length=144)
    resumo = models.TextField(max_length=187,blank=True)
    texto = models.TextField()
    imagem_carrossel = models.ImageField(upload_to='images/' )
    imagem_pequena = models.ImageField(upload_to='images/' )
    imagem_grande = models.ImageField(upload_to='images/' )
    url_comentarios = models.CharField(max_length=500)
    data = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(Categoria,blank=True)

    def dia(self):
        return self.data.date()
    def mes(self):
        return self.data.month()

    def __str__(self):
       return self.titulo












