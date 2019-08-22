from django import template

register = template.Library()


@register.simple_tag
def show_active(request, pattern):
    path = request.path
    if path == pattern:
        return 'active'
    return ''
