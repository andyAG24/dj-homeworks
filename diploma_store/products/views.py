from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

PRODUCTS_PER_PAGE = 3


def product_list_view(request, section_slug=None, category_slug=None):
    products = Product.objects.all()
    category_name = 'Весь ассортимент'

    if section_slug and category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = list(category.products.all())
        category_name = category.name.capitalize()

    page = request.GET.get('page')
    paginator = Paginator(products, PRODUCTS_PER_PAGE)
    products_paginate = paginator.get_page(page)

    context = {
        'category_name': category_name,
        'products_paginate': products_paginate,
    }

    return render(request, 'products/product-list.html', context)


def product_view(request, section_slug, category_slug, slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(category.products, slug=slug)

    context = {'product': product, }

    return render(request, 'products/product.html', context)
