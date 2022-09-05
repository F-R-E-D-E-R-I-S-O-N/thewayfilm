from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "films/index.html", {'title': 'TWF'})


def films_catalog(request):
    return render(request, "films/catalog.html", {'title': 'TWF: films'})


def crew(request):
    return HttpResponse("<h1>на этой странице будут показанa моя команда</h1>")


def news(request):
    return render(request, "films/news.html", {'title': 'TWF: NEWS'})
