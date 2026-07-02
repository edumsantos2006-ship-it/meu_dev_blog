from django.contrib import admin
from .models import Categoria, Artigo

admin.site.register(Categoria)
admin.site.register(Artigo)

class ArtigoAdmin(admin.ModelAdmin):
    list_play = ("titulo", "autor", "categoria", "data_publicacao")

    search_fields = ("titulo", "conteudo")

    list_filter = ("categoria", "data_publicacao")