from django.contrib.auth.models import User
from django.db import models
# from django.db.models.fields import 


class Profile(models.Model):

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'
    
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name = 'пользователь',
    )

    is_privileged = models.BooleanField(
        default=False,
        verbose_name = 'привилегированный',
    )

    def __str__(self):
        return f'{self.user}{" (привилегированный)" if self.is_privileged else ""}'


class Article(models.Model):

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
    
    title = models.CharField(
        max_length = 255,
        verbose_name = 'заголовок',
    )

    image = models.ImageField(
        upload_to = 'images/',
        verbose_name = 'изображение'
    )
    
    text = models.TextField(
        verbose_name = 'текст'
    )

    is_paid = models.BooleanField(
        default=False,
        verbose_name = 'платная',
    )

    def __str__(self):
        return f'{self.title}{" (платная)" if self.is_paid else ""}'
