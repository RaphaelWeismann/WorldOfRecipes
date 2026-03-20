from django import template
import catalog.views as views
from catalog.models import Recipe, Category, TagPost

register = template.Library()

@register.simple_tag(name='getcats')
def get_catalogs():
    return views.cats_db

@register.inclusion_tag('catalog/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected_id}

@register.inclusion_tag('catalog/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}