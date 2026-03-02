from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Здесь вы найдете рецепты всего мира.")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Рецепты по категориям</h1><p>id:{cat_id}</p>")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Рецепты по категориям</h1><p>slug:{cat_slug}</p?")

def archive(self, year):
    return HttpResponse(f"<h1>Рецепты по годам</h1><p>{year}</p>")