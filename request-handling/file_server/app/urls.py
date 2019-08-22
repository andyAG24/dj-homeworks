import datetime as dt
from django.urls import path
from django.urls import register_converter
from .views import *

# Определите и зарегистрируйте конвертер для определения даты
# в урлах и наоборот урла по датам

# def register_converter(converter, type_name):
#     REGISTERED_CONVERTERS[type_name] = converter()
#     get_converters.cache_clear()
# Converter sample:
# class UUIDConverter:
#     regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
#
#     def to_python(self, value):
#         return uuid.UUID(value)
#
#     def to_url(self, value):
#         return str(value)


class DateUrlConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return dt.datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value.date()


register_converter(DateUrlConverter, 'format')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<format:date>/', file_list, name='file_list'),
    path('files/<str:name>/', file_content, name='file_content'),
]
