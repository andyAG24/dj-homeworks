from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование раздела')
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование категории')
    section = models.ForeignKey(
        Section,
        related_name='categories', on_delete=models.PROTECT, verbose_name='Раздел'
    )
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование')
    category = models.ForeignKey(
        Category,
        related_name='products', on_delete=models.PROTECT, verbose_name='Категория'
    )
    product_article = models.IntegerField(blank=False,
                                          verbose_name='Артикул товара', unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    image = models.ImageField(upload_to='img/products/', blank=True, verbose_name='Фото товара')
    price = models.DecimalField(max_digits=10, blank=False, verbose_name='Цена товара', decimal_places=2, default=0)
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
