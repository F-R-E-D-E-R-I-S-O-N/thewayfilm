from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random

def index(request):
    new_film=FilmsCatalog.objects.get(new_film=True)
    random_film = FilmsCatalog.objects.exclude(new_film=True).order_by('?')[1]
    return render(request, "films/index.html", {'new_film': new_film, 'random_film': random_film, 'title': 'TWF'})


def films_catalog(request):
    films = FilmsCatalog.objects.all()
    return render(request, "films/catalog.html", {'films': films, 'title': 'TWF: FILMS'})
    

def view_film(request, title):
    film=FilmsCatalog.objects.get(title_for_url=title)
    return render(request, "films/movie_page.html", {'film': film, 'title': f'TWF: {title.title()}'})

def crew(request):
    return render(request, "films/crew.html", {'title': 'TWF: CREW'})


def news(request):
    films=FilmsCatalog.objects.all()
    return render(request, "films/news.html", {'amount': amount, 'films': films, 'title': 'TWF: NEWS'})
