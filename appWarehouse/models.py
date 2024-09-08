from django.db import models

class Warehouse(models.Model):
    
    title = models.CharField (
        verbose_name="Название склада",
        max_length=50,
        blank=False,
        null=False,
    )
    
    address = models.CharField (
        verbose_name="Адрес склада",
        max_length=255,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'Склады'
        
class Product(models.Model): 
    
    title = models.CharField (
        verbose_name="Название товара",
        max_length=150,
        blank=False,
        null=False,
    ) 
    
    article =  models.CharField (
        verbose_name="Артикул",
        max_length=50,
        default = '0',
        blank=False,
        null=False,
    ) 
    
    price = models.IntegerField(
        verbose_name='Цена',
        null=True, 
        blank=True, 
        default="0"
        )
    
    barcode = models.FileField (
        verbose_name="Баркод",
        upload_to = "barcode/",
        blank=True,
        null=True,
    )
       
    description = models.TextField(
        verbose_name='Описание', 
        null=True, 
        blank=True, 
        default='')
    
    
    warehouse = models.ManyToManyField(
        Warehouse, 
        verbose_name = 'Склад',
        blank=True,
        null=True,
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']
    
    
           