from django.db import models
from django.contrib.auth.models import User

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
        upload_to = "barcode/%Y/%m/%d/",
        blank=True,
        null=True,
    )
       
    description = models.TextField(
        verbose_name='Описание',
        default='-',)
    
    count = models.IntegerField(
        verbose_name='Количество',  
        default=0,)
    
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='image_products/%Y/%m/%d/',
        default='image_products/noimage.png', 
        null=True, 
        blank=True, 
        )    
     
    warehouse = models.ManyToManyField(
        Warehouse, 
        verbose_name = 'Склад',
        blank=True,
        null=True,
        )    
    
    user = models.ForeignKey('auth.User',
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)    
  
  
    def save(self, *args, **kwargs):
        if self.count == 0:
            raise ValueError("Невозможно сохранить продукт с нулевым остатком")
        super().save(*args, **kwargs)

  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']
    
    
class CountRecord(models.Model):    
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=(('in', 'Приход'), ('out', 'Расход')))
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}: {self.action} {self.quantity} шт."   
    
           