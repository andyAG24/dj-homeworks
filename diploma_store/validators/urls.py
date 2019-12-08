from django.contrib import admin
from django.urls import path
from .views import empty_func

urlpatterns = [
    path('', empty_func, name='main'),
    path('admin/', admin.site.urls),

]
