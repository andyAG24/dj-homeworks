from django.db import models


MIN_VALUE = 1 
MAX_VALUE = 1048576


class Player(models.Model):

    class Meta:
        verbose_name='Игрок'
        verbose_name_plural='Игроки'


class Game(models.Model):

    class Meta:
        verbose_name='Игра'
        verbose_name_plural='Игры'
    
    value = models.IntegerField(
        verbose_name='загаданное число'
    )

    creator = models.ForeignKey(
        to='Player',
        on_delete=models.CASCADE,
        related_name='own_games',
        verbose_name='создатель'
    )


class PlayerGameInfo(models.Model):

    class Meta:
        verbose_name='Игровая информация'
        verbose_name_plural='Игровая информация'
    
    player = models.ForeignKey(
        to='Player',
        on_delete=models.CASCADE,
        related_name='games',
        verbose_name='игрок'
    )

    game = models.ForeignKey(
        to='Game',
        on_delete=models.CASCADE,
        related_name='players',
        verbose_name='игра'
    )

    attempts = models.IntegerField(
        default=1,
        verbose_name='попытки'
    )

    min_value = models.PositiveIntegerField(
        default=MIN_VALUE,
        verbose_name='наибольшее возможное значение'
    )

    max_value = models.PositiveIntegerField(
        default=MAX_VALUE,
        verbose_name='наименьшее возможное значение'
    )
