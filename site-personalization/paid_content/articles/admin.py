from django.contrib import admin

from articles.models import Article, Profile


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    pass


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass

