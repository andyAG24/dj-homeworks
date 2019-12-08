from django.shortcuts import render


def empty_func(request):
    template_name = 'base.html'

    context = {}

    return render(request, template_name, context)
