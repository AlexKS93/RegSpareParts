# Generated by Django 2.2.16 on 2023-05-05 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reg', '0005_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='SparePartsEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('POST', 'Создание'), ('DELETE', 'Удаление'), ('PATCH', 'Изменение')], max_length=150, verbose_name='Наименование')),
                ('message', models.TextField(verbose_name='Наименование')),
                ('table_name', models.CharField(max_length=150, verbose_name='Таблица')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('id_record', models.ForeignKey(on_delete='Запись', to='reg.Categoryes')),
                ('user', models.ForeignKey(on_delete='Пользователь', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]