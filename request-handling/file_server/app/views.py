import datetime as dt
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import os

FILES_ARRAY = os.listdir(settings.FILES_PATH)


def file_list(request, date=None):
    template_name = 'index.html'
    all_files = []
    context = {}

    if date:
        context['date'] = date.date()

    for file in FILES_ARRAY:
        file_stat = os.stat(f'{settings.FILES_PATH}/{file}')
        file_info = {
            'name': file,
            'ctime': dt.datetime.fromtimestamp(file_stat.st_ctime),
            'mtime': dt.datetime.fromtimestamp(file_stat.st_mtime),
        }
        all_files.append(file_info)
    return render(request, template_name, context={'files': all_files})


def file_content(request, name):
    file_path = os.path.join(settings.FILES_PATH, name)
    if os.path.exists(file_path):
        with open(os.path.join(settings.FILES_PATH, name),
                  encoding='utf-8') as f:
            file_data = f.read()
        return render(
            request,
            'file_content.html',
            context={
                'file_name': name,
                'file_content': file_data
            }
        )
    else:
        return HttpResponse("Ошибка 404. Запрошенный файл не существует", status=404)
