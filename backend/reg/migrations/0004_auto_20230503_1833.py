# Generated by Django 2.2.16 on 2023-05-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_auto_20230503_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spareparts',
            name='note',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='tmc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ТМЦ'),
        ),
    ]
