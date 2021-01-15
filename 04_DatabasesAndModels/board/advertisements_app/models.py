from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True)
    description = models.TextField(default='', null=True, verbose_name='Описание')
    price = models.FloatField(null=True, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    finish_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    advertisement_heading = models.ForeignKey('Heading', default=None, null=True, on_delete=models.CASCADE,
                                              related_name='ad_status')
    advertisement_type = models.ForeignKey('Type', default=None, null=True, on_delete=models.CASCADE,
                                           related_name='ad_type')
    advertisement_author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE,
                                             related_name='ad_author')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Heading(models.Model):
    advertisement_status = models.CharField(max_length=20)

    def __str__(self):
        return self.advertisement_status

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Type(models.Model):
    advertisement_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.advertisement_type


class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.last_name
