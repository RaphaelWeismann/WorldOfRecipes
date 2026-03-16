from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from .models import Recipe

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Recipe.published.all()
    data = {
        'title': 'главная страница',
        'posts': posts,
        'menu': menu,
        'cat_selected': 0,
        }
    return render(request, 'catalog/index.html', context=data)

def about(request):
    return render(request, 'catalog/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Recipe, slug=post_slug)
    data = {
        'title': post.title,
        'menu':menu,
        'post':post,
        'cat_selected': 1,
    }
    
    return render(request, 'catalog/post.html', context=data)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по категориям',
        'posts': Recipe.published.all(),
        'menu': menu,
        'cat_selected': cat_id,
        }
    return render(request, 'catalog/index.html', context=data)

cats_db = [
    {'id': 1, 'name': 'Завтрак'},
    {'id': 2, 'name': 'Обед'},
    {'id': 3, 'name': 'Ужин'},
]