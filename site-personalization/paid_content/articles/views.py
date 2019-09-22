from django.shortcuts import render

from articles.models import Article, Profile


def show_articles(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):

    article = Article.objects.get(pk=id)
    
    print(article.image)

    if article.is_paid:
        profile = getattr(request.user, 'profile', None)
        if not profile or not profile.is_privileged:
            article = {
            'title': article.title,
            'text': 'Для того, чтобы читать данную статью, необходимо подписаться на журнал!',
            'image': article.image
        }
        
    context = {
        'article': article
    }
    
    return render(
        request,
        'article.html',
        context
    )
