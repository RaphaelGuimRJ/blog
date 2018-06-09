from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from castnautas.forms import *
from castnautas.models import *

# Create your views here.

def index(request,page_num=1):

    if request.method == 'GET':
        postagens = Postagem.objects.order_by('-data')
        pages = Paginator(postagens, 8)

        carrossel = Postagem.objects.order_by('-data')

        carr = Paginator(carrossel,3)

        lista_carr = carr.page(1).object_list

        if int(page_num) > pages.num_pages or int(page_num) == 0:
            page_num = 1

        page = pages.page(page_num).object_list
        form = BuscaForm()

    else:

        categoria = request.POST['categorias']

        return redirect('busca', tag=categoria, page_num=1)

    return render(request,'index.html',{'postagens':page,'carrossel':lista_carr,'page_num':page_num, 'form':form})

def post(request, post_num):

    postagem =list(Postagem.objects.filter(pk=post_num))

    if len(postagem) == 0:
        return redirect ('index')

    else:
        postagem = postagem[0]
        return render(request,'post.html',{'postagem':postagem})

def busca(request,tag,page_num=1):
    if request.method =='GET':
        categorias = list(Categoria.objects.filter(nome=tag))

        if len(categorias) == 0:
            return redirect ('index')

        else:
            categoria = categorias[0]
            postagens = Postagem.objects.filter(categorias=categoria)
            pages = Paginator(postagens, 8)

        carrossel = Postagem.objects.order_by('-data')

        carr = Paginator(carrossel, 3)

        lista_carr = carr.page(1).object_list

        if int(page_num) > pages.num_pages or int(page_num) == 0:
            page_num = 1

        page = pages.page(page_num).object_list

    else:

        categoria = request.POST['categorias']

        return redirect('busca', tag=categoria, page_num=1)

    return render(request, 'index.html', {'postagens': page, 'carrossel': lista_carr, 'page_num': page_num, 'form': BuscaForm()})