from django.http import HttpResponse

def home(request):
    mensagem = "<h1>Bem_Vindo ao DevBlog!</h1> <p> Em breve, artigos aqui.</p>"

    return HttpResponse(mensagem)

def sobre_nos(request):
    mensagem_2 = "<h1>Sobre o DevBlog:</h1 <p> Esse é meu primeiro DevBlog, estou muito empolgado!!</p>"

    return HttpResponse(mensagem_2)
