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
    imagem_carrossel = models.ImageField(upload_to='images/', blank=True, null=True )
    imagem_pequena = models.ImageField(upload_to='images/',  blank=True, null=True)
    imagem_grande = models.ImageField(upload_to='images/',  blank=True, null=True )
    arquivo_audio = models.FileField(upload_to='audios/', blank=True, null=True)
    url_comentarios = models.CharField(max_length=500)
    data = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(Categoria,blank=True)
    visitas = models.IntegerField(default=0)
    plays = models.IntegerField(default=0)

    def dia(self):
        return self.data.date()
    def mes(self):
        return self.data.month

    def __str__(self):
       return self.titulo

    def visitas_relatorio(self):
        visitas = Visita.objects.filter(postagem=self)
        cidades = {}
        for visita in visitas:
            print(cidades)
            if not visita.cidade in cidades:
                cidades[visita.cidade] = 1
            else:
                cidades[visita.cidade] = cidades[visita.cidade] + 1

        return cidades

class Visita(models.Model):
     postagem = models.ForeignKey(Postagem,on_delete=models.CASCADE)
     cidade = models.TextField(null=False,)











