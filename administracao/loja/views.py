from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def pesquisar(request):

    if request.method == 'POST':
        print("METODO POST")
        pesquisa = request.POST.get('pesquisa')
        produto = Produto.objects.filter(nome__contains = pesquisa)
        print(produto)
        return render(request,'loja/pesquisar.html',{'produto': produto})


    produto = Produto.objects.all()
    return render(request,'loja/pesquisar.html',{'produto': produto})
    #return HttpResponse(produto)


def cadastrar(request):

    return HttpResponse("Cadastrando")

