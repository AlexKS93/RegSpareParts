# Generated by Django 2.2.16 on 2023-05-03 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_auto_20230503_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryes',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='manufacturers',
            options={'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
    ]
