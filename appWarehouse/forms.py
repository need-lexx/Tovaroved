from django import forms
from .models import Product, Warehouse


class AddProductForm(forms.Form):
    title= forms.CharField(max_length=255, label="Наименование")
    article=forms.CharField(max_length=50, label="Артикул")
    price=forms.IntegerField(required=False, label="Цена")
    barcode=forms.FileField(required=False, label="Баркод")
    description=forms.CharField(widget=forms.Textarea(), required=False, label="Описание")
    # warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(), empty_label="Не выбрано", label="Склад")
    
  
    