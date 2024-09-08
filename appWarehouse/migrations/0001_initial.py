# Generated by Django 5.1 on 2024-09-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название склада')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес склада')),
            ],
            options={
                'verbose_name': 'склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название товара')),
                ('article', models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Артикул')),
                ('price', models.IntegerField(default='0', verbose_name='Цена')),
                ('barcode', models.FileField(upload_to='barcode/', verbose_name='Баркод')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('warehouse', models.ManyToManyField(blank=True, null=True, to='appWarehouse.warehouse')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['title'],
            },
        ),
    ]
