# Дипломный проект по курсу «Django: создание функциональных веб-приложений»

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Провести миграцию:

```bash
python3 manage.py migrate
```

* Команда для создания пользователя без проверки пароля на сложность 
```bash
python3 manage.py createadmin
```


Загрузить тестовые данные:

```bash
python3 manage.py loaddata fixtures.json
```


Запустить отладочный веб-сервер проекта:

```bash
python3 manage.py runserver
```