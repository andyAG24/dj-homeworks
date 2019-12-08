from django.db import models

from products.models import Product


class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    products = models.ManyToManyField(Product, verbose_name='Соответствующие товары', blank=True)
    author = models.CharField(max_length=100, default='Иванов Артем', verbose_name='Автор статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
