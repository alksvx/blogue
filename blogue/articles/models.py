from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

categories = [
    ('Красота', 'Красота'),
    ('Мода', 'Мода'),
    ('Отношения', 'Отношения'),
    ("Знаменитости", "Знаменитости"),
]

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг')
    body = models.TextField(verbose_name='Статья')
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpeg', blank=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.CharField(choices=categories, default='Мода', max_length=15, verbose_name='Категория')


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:500] + '...'

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.slug)])