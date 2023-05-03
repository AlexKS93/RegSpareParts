from django.db import models


class Manufacturers(models.Model):
    name = models.CharField("Наименование",
                            max_length=150)
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return f'{self.name}'

class Categoryes(models.Model):
    name = models.CharField("Наименование",
                            max_length=150)
    
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
    change_date = models.DateTimeField("Дата изменения")
    create_date = models.DateTimeField("Дата добавления")
    review_date = models.DateTimeField("Дата ревизии")

    class Meta:
        verbose_name = 'Запасная часть'
        verbose_name_plural = 'Запасные части'

    def __str__(self):
        return f'{self.name}'