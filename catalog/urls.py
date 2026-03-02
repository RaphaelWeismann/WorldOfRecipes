from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:cat_id>/', views.categories, name='cat_id'),
    path('<slug:cat_slug>/', views.categories_by_slug, name='cat_slug'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]