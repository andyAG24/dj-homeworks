from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    minutes_gone = (datetime.timestamp(datetime.now()) - value) / 60
    hours_gone = round(minutes_gone / 60)
    if minutes_gone < 10:
        return 'только что'
    if hours_gone < 24:
        if hours_gone in [1, 21]:
            return f'{hours_gone} час назад'
        if hours_gone in [2, 3, 4, 22, 23]:
            return f'{hours_gone} часа назад'
        return f'{hours_gone} часов назад'
    return datetime.fromtimestamp(value).date().strftime("%Y-%m-%d")


@register.filter
def format_score(value):
    if value <= -5:
        return 'все плохо'
    if -5 < value <= 5:
        return 'нейтрально'
    if value > 5:
        return 'хорошо'


@register.filter
def format_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    if 0 < value <= 50:
        return value
    if value > 50:
        return '50+'


@register.filter
def format_text(value, count):
    words_count = len(value.split())
    if words_count > count * 2:
        format_value = ' '.join(value.split()[:count] + ['...'] + value.split()[-count:])
        return format_value
    return value
