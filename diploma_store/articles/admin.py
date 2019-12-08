from django.contrib import admin

from .models import Article
from .forms import ArticleAdminForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')

class ArticleAdminReviewForm(admin.ModelAdmin):
    form = ArticleAdminForm


admin.site.register(Article, ArticleAdminReviewForm)
