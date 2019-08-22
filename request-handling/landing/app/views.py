from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    index_name = request.GET.get('from-landing')
    if index_name in ['original', 'test']:
        counter_click[index_name] += 1
    return render_to_response('index.html')


def landing(request):
    index_name = request.GET.get('ab-test-arg')
    counter_show[index_name] += 1
    if index_name == 'test':
        return render_to_response('landing_alternate.html')
    elif index_name == 'original':
        return render_to_response('landing.html')
    else:
        return HttpResponse('Ошибка перехода', status=400)


def stats(request):
    if counter_show['test']:
        counter_test = counter_click['test'] / counter_show['test']
    else:
        counter_test = 0

    if counter_show['original']:
        counter_original = counter_click['original'] / counter_show['original']
    else:
        counter_original = 0

    return render_to_response('stats.html', context={
        'test_conversion': counter_test,
        'original_conversion': counter_original,
    })
