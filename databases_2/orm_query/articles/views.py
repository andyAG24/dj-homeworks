from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'


# https://dizballanze.com/ru/django-project-optimization-part-2/
# defer откладывает получение полей переданных в качестве аргументов,
# only откладывает получение всех полей, кроме переданных.
# Метод select_related работает только с внешними ключами в текущей модели
# , для того, чтобы уменьшить количество запросов при получении множества
# связанных объектов (таких как теги в нашем примере), нужно использовать
# метод prefetch_related

    def get_queryset(self):

        return self.model.objects.only(
            'author', 'genre')

