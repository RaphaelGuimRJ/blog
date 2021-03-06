import requests
from django.core.paginator import Paginator
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ipware import get_client_ip



from castnautas.forms import *
from castnautas.models import *


# Create your views here.

def index(request, page_num=1):
    if request.method == 'GET':
        postagens = Postagem.objects.order_by('-data')
        pages = Paginator(postagens, 6)
        carr = Paginator(postagens, 3)
        lista_carr = carr.page(1).object_list

        try:
            page = pages.get_page(page_num)
        except:
            page = pages.get_page(1)

        form = BuscaForm()

    else:

        categoria = request.POST['categorias']

        return redirect('busca', tag=categoria, page_num=1)
    context = {'postagens': page,
               'carrossel': lista_carr,
               'page_num': page_num,
               'form': form,
               'titulo': 'Castnautas',
               'descricao': 'Em uma galáxia não tão distante, onde o espaço ainda não é a fronteira final e todo mundo pode te ouvir gritar, Dio, Gabs, Nanda e Rapha mandam saudações ao planeta Terra para avisar que está no ar o podcast mais bacanudo deste lado do universo! Prepare seus fones de ouvido, não esqueça sua toalha e sempre tenha em mãos algumas batatas para viajar com os Castnautas!',

               }
    return render(request, 'index.html',
                  context)


def post(request, titulo):
    if request.method == 'GET':
        titulo = str(titulo).replace('-', ' ')
        postagem = list(Postagem.objects.filter(titulo__iexact=titulo))

        if len(postagem) == 0:
            return redirect('index')

        else:
            postagem = postagem[0]
            postagem.visitas =  postagem.visitas +1
            postagem.save()

            context = {
                'postagem': postagem,
                'form': BuscaForm(),
                'titulo': postagem.titulo,
                'descricao': postagem.resumo,

            }
            return render(request, 'post.html', context)
    else:
        categoria = request.POST['categorias']

        return redirect('busca', tag=categoria, page_num=1)


def busca(request, tag, page_num=1):
    if request.method == 'GET':
        categorias = list(Categoria.objects.filter(nome=tag))

        if len(categorias) == 0:
            return redirect('index')

        else:
            categoria = categorias[0]
            postagens = Postagem.objects.filter(categorias=categoria).order_by('-data')
            pages = Paginator(postagens, 6)

        carrossel = Postagem.objects.order_by('-data')
        carr = Paginator(carrossel, 3)
        lista_carr = carr.page(1).object_list

        try:
            page = pages.get_page(page_num)
        except:
            page = pages.get_page(1)


    else:

        categoria = request.POST['categorias']

        return redirect('busca', tag=categoria, page_num=1)

    context = {
        'postagens': page,
        'carrossel': lista_carr,
        'page_num': page_num,
        'form': BuscaForm(),
        'tag': tag
    }

    return render(request, 'index.html', context)


def plays(request):

    try:
        post = Postagem.objects.get(pk=request.GET.get('post'))

        post.plays = post.plays + 1
        post.save()

        try:
            ip, is_routable = get_client_ip(request)

            if ip and is_routable:
                chamada = "http://api.ipstack.com/" + ip + "?access_key=beda9dfa1853ae5fe5bf8756f2ff4683"
                r = requests.get(chamada).json()
                visita = Visita(post,r['city'])
                visita.save()
        except:
            pass

        return HttpResponse('Sucesso em salvar o número de plays')
    except:
        print("Falhou")
        return HttpResponse('Falhou em salvar o número de plays')



