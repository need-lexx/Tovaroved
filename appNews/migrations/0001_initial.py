# Generated by Django 5.1 on 2024-09-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Контент')),
                ('dtime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('status', models.BooleanField(choices=[(True, 'Обликовано'), (False, 'Не опубликовано')], default=False, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
