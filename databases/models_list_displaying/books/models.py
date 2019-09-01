from django.db import models


class Book(models.Model):
    name = models.CharField(u'Название', max_length=100)
    author = models.CharField(u'Автор', max_length=100)
    pub_date = models.DateField(u'Дата публикации', max_length=20)

    def __str__(self):
        return self.name + " " + self.author
