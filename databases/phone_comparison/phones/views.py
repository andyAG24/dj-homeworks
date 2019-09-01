from django.shortcuts import render
from .models import *


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    # samsung = Samsung.objects.first()
    # xiaomi = Xiaomi.objects.first()
    # iphone = Iphone.objects.first()

    context = {'phones': phones}

    return render(
        request,
        template,
        context
    )

