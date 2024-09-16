from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from .forms import AddProductForm
from .models import Product


class PersonAccount (View):
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated and request.user.is_active:
            return super().dispatch(request, *args, **kwargs)
        return redirect('urlPageHome')

    def get(self, request):
        
        # products = Product.objects.all() 
       
        
        # for product in products:
        #     Product.objects.filter().values('id', 'title', 'article', 'price')
        #     print(product.title)
            
            
             
        return render(request, 'appWarehouse/index.html')


def addProduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            try:                
                Product.objects.create(**form.cleaned_data)
                return redirect("urlPersonalAccount")
            except:  
                form.add_error(None, "Ошибка добавления товара!")  
    else:
        form = AddProductForm()
    data = {
        'form': form
    }
    return render(request, 'appWarehouse/addproduct.html', data)


class AddWarehouse (View):
    def get(self, request):
        return render(request, 'appWarehouse/addwarehouse.html')
    
class IncomeProduct (View):
    def get(self, request):
        return render(request, 'appWarehouse/income_product.html')
    
class ExpenseProduct (View):
    def get(self, request):
        return render(request, 'appWarehouse/expense_product.html')
