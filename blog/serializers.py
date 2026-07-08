from rest_framework import serializers
from .models import Artigo, Categoria

class ArtigoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = ['id', 'titulo', 'categoria', 'autor', 'conteudo', 'data_publicacao']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']