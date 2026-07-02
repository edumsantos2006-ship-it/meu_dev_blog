from django.shortcuts import render
from .models import Artigo, Categoria


def home(request):
    
    noticias = Artigo.objects.all()
    categorias = Categoria.objects.all()


    contexto = {
        'lista_artigos' : noticias,
        'lista_categorias' : categorias
    }
    return render(request, 'blog/index.html', contexto)

def sobre_nos(request):
    categorias = Categoria.objects.all()

    contexto = {
        'lista_categorias': categorias
    }

    return render(request, 'blog/sobre.html', contexto)

def categoria(request, id):
    artigos = Artigo.objects.filter(categoria_id=id)
    categorias = Categoria.objects.all()

    contexto = {
        'lista_artigos': artigos,
        'lista_categorias': categorias,
    }

    return render(request, 'blog/index.html', contexto)
    


