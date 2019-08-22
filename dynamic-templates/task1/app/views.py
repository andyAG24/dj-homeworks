from django.shortcuts import render
from .settings import CSV_FILE
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    with open(CSV_FILE) as f:
        result = list(csv.reader(f, delimiter=';'))

    context = {'data': result}

    return render(request, template_name, context)
