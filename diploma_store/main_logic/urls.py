from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import home_view
from customers.views import login_view, logout_view, signup_view, order_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('order/', order_view, name='order'),
    path('', home_view, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
