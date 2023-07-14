
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Manufacturers(models.Model):
    name = models.CharField("Наименование",
                            max_length=150,
                            unique=True,
                            null=False)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return f'{self.name}'


class Categoryes(models.Model):
    name = models.CharField("Наименование",
                            max_length=150,
                            unique=True,
                            null=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class SpareParts(models.Model):
    name = models.CharField("Наименование",
                            max_length=150)
    tmc = models.CharField("ТМЦ",
                           max_length=150,
                           null=True,
                           blank=True)
    manufacturer = models.ForeignKey(Manufacturers,
                                     "Производитель")
    category = models.ForeignKey(Categoryes,
                                 "Категория")
    count = models.IntegerField("Количество")
    note = models.CharField("Примечание",
                            max_length=1024,
                            null=True,
                            blank=True)
    place = models.CharField("Место",
                             max_length=150)
    floor = models.IntegerField("Этаж")
    change_date = models.DateTimeField("Дата изменения", auto_now=True)
    create_date = models.DateTimeField("Дата добавления", auto_now=True)
    review_date = models.DateTimeField("Дата ревизии", auto_now=True)

    class Meta:
        verbose_name = 'Запасная часть'
        verbose_name_plural = 'Запасные части'

    def __str__(self):
        return f'{self.name}'


class Events(models.Model):
    CHOICES = (
        ('POST', 'Создание'),
        ('DELETE', 'Удаление'),
        ('PATCH', 'Изменение'),
    )
    event_type = models.CharField("Наименование",
                                  max_length=150,
                                  choices=CHOICES)
    message = models.TextField("Наименование")
    data = models.TextField("Данные",
                            default="")
    user = models.ForeignKey(User,
                             "Пользователь")
    create_date = models.DateTimeField("Дата", auto_now=True)

    class Meta:
        abstract = True


class CategoryesEvents(Events):
    id_record = models.ForeignKey(Categoryes,
                                  "Запись")

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f'{self.event_type} | {self.user} | {self.message}'
    
class SparePartsEvents(Events):
    id_record = models.ForeignKey(SpareParts,
                                  "Запись")

    class Meta:
        verbose_name = 'Событие журнала ЗИП'
        verbose_name_plural = 'События журнала ЗИП'

    def __str__(self):
        return f'{self.event_type} | {self.user} | {self.message}'
