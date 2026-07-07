from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Categoria
from .forms import ContatoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtigoSerializers, CategoriaSerializer


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

def fale_conosco(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    
    else:
        formulario = ContatoForm()

    contexto = {
        'lista_categorias': categorias,
        "form ": formulario
    }
    
    return render(request, 'blog/contato.html', {'form' : formulario})


@api_view(['GET'])
def api_listar_artigos(request):
    artigos = Artigo.objects.all()
    serializer = ArtigoSerializers(artigos, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def api_listar_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)

    return Response(serializer.data)