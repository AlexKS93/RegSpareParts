# Generated by Django 2.2.16 on 2023-05-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spareparts',
            options={'verbose_name': 'Запасная часть', 'verbose_name_plural': 'Запасные части'},
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='note',
            field=models.CharField(max_length=1024, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='tmc',
            field=models.CharField(max_length=150, null=True, verbose_name='ТМЦ'),
        ),
    ]