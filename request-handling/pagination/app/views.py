import csv
from django.core.paginator import Paginator
from django.conf import settings
from urllib.parse import urlencode
from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def open_csv(file_name):
    with open(file_name, newline='', encoding='cp1251') as f:
        reader = list(csv.DictReader(f))
    return reader


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page = request.GET.get('page', 1)
    if not page:
        page = 1

    paginator = Paginator(open_csv(settings.BUS_STATION_CSV), 10, orphans=5)
    post = paginator.page(page)

    if post.has_previous():
        prev_page = '?'.join([reverse(bus_stations), urlencode({'page': post.previous_page_number()})])
    else:
        prev_page = ''
    if post.has_next():
        next_page = '?'.join([reverse(bus_stations), urlencode({'page': post.next_page_number()})])
    else:
        next_page = ''

    return render_to_response('index.html', context={
        'bus_stations': post.object_list,
        'current_page': page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })
