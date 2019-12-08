from django.contrib import admin
from .models import *


class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'slug',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_article', 'category', 'price', )


admin.site.register(Section, SectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
