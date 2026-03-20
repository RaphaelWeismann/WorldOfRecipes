from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from .models import Recipe, Category, TagPost

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
        'cat_selected': post.cat.id,
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

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Recipe.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'posts': posts,
        'menu': menu,
        'cat_selected': category.pk,
        }
    return render(request, 'catalog/index.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Recipe.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'catalog/index.html', context=data)