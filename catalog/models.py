from django.db import models
from django.urls import reverse

# Create your models here.
class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Recipe.Status.PUBLISHED)

class Recipe(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, 
                                       default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name=
                            'posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    nutrition = models.OneToOneField('Nutrition', on_delete=models.SET_NULL,
                                     null=True, blank=True, 
                                     related_name='recipe')

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    objects = models.Manager()
    published = PublishedModel()

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
    
class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.tag

class Nutrition(models.Model):
    calories = models.IntegerField(null=True)
    protein = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    carbs = models.FloatField(null=True)

    def __str__(self):
        return f"{self.calories} ккал"