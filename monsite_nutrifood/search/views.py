from django.shortcuts import render
from django.http import HttpResponse
from search.models import Produit


def index(request):
    # obj = Produit.objects.all()

    obj = Produit.objects.filter(cat__name_cat="Boissons")

    output = []

    for i in obj:
        output.append(i.nom_P + "\n")

    return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the
    #
    #  search index.")


def lala(request):
    return HttpResponse("lala")
