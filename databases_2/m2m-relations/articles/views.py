from django.db.models import Prefetch
from django.shortcuts import render
from articles.models import *


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    ordering = '-published_at'  # сортируем статьи по дате

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # The negative sign in front of "-pub_date" indicates descending order.
    # Ascending order is implied. To order randomly, use "?"
    articles = Article.objects.order_by(ordering).prefetch_related(
        Prefetch('scopes', queryset=ArticleScope.objects.order_by(
            '-is_main').select_related('topic')))

    context['object_list'] = articles

    return render(request, template, context)
