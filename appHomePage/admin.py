from django.contrib import admin
from .models import ReturnRequest

@admin.register(ReturnRequest)
class ReturnRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email', 'status', 'dtime']
    list_display_links = ['id', 'first_name', 'email']
    list_filter = ['status']
    ordering = ['dtime']
    list_editable = ['status']
