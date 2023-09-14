from django.db import models

class Block_massag(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    time = models.CharField(null=True, blank=True,max_length=10, verbose_name="Продолжительность в минутах")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    PoleOt = models.CharField(null=True, blank=True,max_length=2, verbose_name="Приставка к сумме")
    price = models.IntegerField(verbose_name="Стоймость")


    class Meta:
        verbose_name_plural = "Услуги массажа"
        verbose_name = "Массаж"


class Block_spa_program(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    time = models.IntegerField(verbose_name="Продолжительность в минутах")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Стоймость")


    class Meta:
        verbose_name_plural = "Спа-программы"
        verbose_name = "Спа-программа"


class Block_taping(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(null=True, blank=True,upload_to='image/taping', verbose_name="Изображение к услуги")
    image2 = models.ImageField(null=True, blank=True,upload_to='image/taping', verbose_name="Изображение к услуги")
    PoleOt = models.CharField(null=True, blank=True, max_length=2, verbose_name="Приставка к сумме")
    price = models.IntegerField(verbose_name="Стоймость")


    class Meta:
        verbose_name_plural = "Тейпирование"
        verbose_name = "Тейпирование"


class Block_obuchine(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    time = models.CharField(null=True, blank=True,max_length=200, verbose_name="Продолжительность")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Стоймость")


    class Meta:
        verbose_name_plural = "Услуга обучения"
        verbose_name = "Обучение"