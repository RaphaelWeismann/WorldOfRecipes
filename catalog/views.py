from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Здесь вы найдете рецепты всего мира.")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Рецепты по категориям</h1><p>id:{cat_id}</p>")

def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Рецепты по категориям</h1><p>slug:{cat_slug}</p?")

def archive(self, year):
    if year > 2026:
        return redirect ('home')
    
    return HttpResponse(f"<h1>Рецепты по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')