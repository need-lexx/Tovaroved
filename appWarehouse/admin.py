from django.contrib import admin
from .models import Warehouse, Product

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "address"]
    list_display_links = ["id", "title", "address"]    
    search_fields = ["title"]
    

@admin.register(Product)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "article"]
    list_display_links = ["id", "title", "article"]   
    search_fields = ["title"]