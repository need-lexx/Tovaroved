from django import forms
from .models import Product, Warehouse
from django.contrib.auth.models import User


class AddProductForm(forms.ModelForm):     
    class Meta:
      model = Product
      fields = ['title', 'article', 'price', 'count', 'image', 'description']
      
      

class ChangeProductCount(forms.Form):  
    quantity = forms.IntegerField(label="Введите количество",)
    action = forms.ChoiceField(label="Действие", choices=[('increase', 'Приход'), ('decrease', 'Расход')])
    
    
    
    # widget=forms.NumberInput(attrs={'id':"exampleInputNumber", 'class':"animated-input"})
 
    

  
    