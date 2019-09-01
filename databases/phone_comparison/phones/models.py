from django.db import models


class Phone(models.Model):
    model = models.CharField(max_length=20, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Цена')
    os = models.CharField(max_length=15, verbose_name='Операционная система')
    sim = models.CharField(max_length=1, verbose_name='Количество SIM-карт')
    memory = models.CharField(max_length=5, verbose_name='Объём оперативной памяти')
    gps = models.BooleanField(default=False, verbose_name='GPS')
    fmradio = models.BooleanField(default=False, verbose_name='FM-Радио')

    def __str__(self):
        return f' {self.model}'

    
    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'
        ordering = ['price']
    

class Samsung(models.Model):
    phone = models.ForeignKey('Phone', null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Samsungs'
        verbose_name_plural = 'Samsung'

    
class Xiaomi(models.Model):
    phone = models.ForeignKey('Phone', null=True, on_delete=models.CASCADE)
    fingerprint = models.BooleanField(default=False, verbose_name='Сканер отпечатка пальцев')

    class Meta:
        verbose_name = 'Xiaomi'
        verbose_name_plural = 'Xiaomis'


class Iphone(models.Model):
    phone = models.ForeignKey('Phone', null=True, on_delete=models.CASCADE)
    pods = models.BooleanField(default=True, verbose_name='Air pods')

    class Meta:
        verbose_name = 'Iphone'
        verbose_name_plural = 'Iphones'



