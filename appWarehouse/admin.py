from django.contrib import admin
from .models import Warehouse, Product
from django.utils.safestring import mark_safe

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "address"]
    list_display_links = ["id", "title", "address"]    
    search_fields = ["title"]
    

@admin.register(Product)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = [ "id", 'product_image',"title", "article","count","user"]
    list_display_links = ["id", 'product_image', "title", "article", "user"]    
    ordering = ["user", "title"]
    list_per_page = 20
    
    @admin.display(description='Изображение товара')
    
    def product_image(self, product: Product):
        if product.image: 
             return mark_safe(f"<img src='{product.image.url}' width=50>")
        return 'Без изображения'
    
    
    
    
    
    
    
    

        
    






    
  