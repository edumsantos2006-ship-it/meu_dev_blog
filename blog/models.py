from django.db import models

# Tabale de Categorias
class Categoria(models.Model):
    #Coluna de texto curto(maximo de 100 caracteres)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
# Tabela de Artigos
class Artigo(models.Model):
    titulo = models.CharField(max_length=200)

    #texto longo, sem limite de caracteres
    conteudo = models.TextField()

    #preenche com a data/hora exata do cadastro
    data_publicacao = models.DateTimeField(auto_now_add=True)

    #relação com a categoria( foreignkey = chave estrangeira)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    autor = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.titulo

