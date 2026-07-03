from django.shortcuts import render, get_object_or_404
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

def artigo_detalhe(request, id):
    noticia = get_object_or_404(Artigo, id=id)

    contexto = {
        'artigo': noticia
    }    
    return render(request, 'blog/artigo_detalhe.html', contexto)


