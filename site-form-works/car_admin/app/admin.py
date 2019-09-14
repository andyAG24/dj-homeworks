from django.contrib import admin

from .models import *
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'get_reviews')
    filter = ('brand', 'model')
    search_fields = ('brand', 'model')
    ordering = ('pk',)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title',)
    filter = ('title', 'car',)
    search_fields = ('car__model',)


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
