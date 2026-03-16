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

recipes_db = [
    {
        'id': 1,
        'title': 'Борщ с пампушками',
        'content': '''<h2>Борщ с пампушками</h2>
<p>Борщ — это душа украинской и русской кухни. Наваристый, ярко-красный, с богатым вкусом свёклы и томата.</p>
<p>Для приготовления понадобится: говяжья грудинка, свёкла, капуста, картофель, морковь, лук, томатная паста и чеснок.
Бульон варится не менее двух часов, чтобы мясо стало мягким и отдало весь вкус.</p>
<p>Пампушки — маленькие мягкие булочки с чесночной заливкой — подаются горячими прямо к тарелке борща.</p>''',
        'is_published': True
    },
    {
        'id': 2,
        'title': 'Паста Карбонара',
        'content': '''<h2>Паста Карбонара</h2>
<p>Классическое блюдо римской кухни. Настоящая карбонара готовится без сливок — только яйца, сыр пекорино, гуанчиале и чёрный перец.</p>
<p>Секрет в технике: яично-сырная смесь вводится в горячую пасту вне огня, чтобы получился кремовый соус, а не яичница.</p>
<p>Гуанчиале — вяленые свиные щёки — обжариваются до хрустящей корочки и придают блюду неповторимый аромат.</p>''',
        'is_published': True
    },
    {
        'id': 3,
        'title': 'Десерт Тирамису',
        'content': '''<h2>Десерт Тирамису</h2>
<p>Тирамису — итальянский десерт без выпечки на основе сыра маскарпоне, яиц, сахара и савоярди.</p>
<p>Печенье савоярди пропитывается крепким эспрессо с добавлением амаретто, затем выкладывается слоями
с кремом из взбитых желтков и маскарпоне.</p>
<p>Десерт должен провести в холодильнике не менее четырёх часов — тогда он приобретёт нужную текстуру и вкус.</p>''',
        'is_published': True
    },
]


def index(request):
    posts = Recipe.objects.filter(is_published=1)
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
        'posts': recipes_db,
        'menu': menu,
        'cat_selected': cat_id,
        }
    return render(request, 'catalog/index.html', context=data)

cats_db = [
    {'id': 1, 'name': 'Завтрак'},
    {'id': 2, 'name': 'Обед'},
    {'id': 3, 'name': 'Ужин'},
]