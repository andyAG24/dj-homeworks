from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import getpass



class Command(BaseCommand):

    help = 'Создание superuser пользователя'

    def handle(self, *args, **kwargs):
        default_username = 'admin'
        default_email = 'admin@admin.biz'

        username = input(f'Введите логин или оставьте поле пустым (логин по умолчанию -  {default_username}): ')
        if username is '':
            username = default_username

        email = input(f'Введите email или оставьте поле пустым (email по умолчанию -  {default_email}): ')
        if email is '':
            email = default_email

        password_one = getpass.getpass('Введите пароль: ')


        if password_one.strip() == '':
            self.stderr.write("Пароль не может быть пустым!")
            password_one = getpass.getpass('Введите пароль заново: ')

        password_two = getpass.getpass('Повторите пароль: ')
        if password_one != password_two:
            password_two = getpass.getpass("Пароль введен неправильно! "
                                           "Пожалуйста, повторите ввод.")

        User.objects.create_superuser(username=username,
                                      email=email,
                                      password=password_one,
                                      )
        print('Superuser успешно создан')
