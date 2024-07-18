from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def pesquisar(request):
    produto = Produto.objects.all()
    return render(request,'loja/pesquisar.html',{'produto': produto})
    #return HttpResponse(produto)


def cadastrar(request):

    return HttpResponse("Cadastrando")

