from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
        
            
        return render(request, 'appWarehouse/index.html', {
            'products' : Product.objects.all()[:50]
        })


def addProduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
        #     try:                
        #         Product.objects.create(**form.cleaned_data)
        #         return redirect("urlPersonalAccount")
        #     except:  
        #         form.add_error(None, "Ошибка добавления товара!")  
            form.save()
            return redirect("urlPersonalAccount")
    else:
        form = AddProductForm()
    data = {
        'form': form
    }
    return render(request, 'appWarehouse/add_product.html', data)


class AddWarehouse (View):
    def get(self, request):
        return render(request, 'appWarehouse/add_warehouse.html')
    
class IncomeProduct (View):
    def get(self, request):
        return render(request, 'appWarehouse/income_product.html')
    
class ExpenseProduct (View):
    def get(self, request):
        return render(request, 'appWarehouse/expense_product.html')
    
class ProductPage(View):
    def get(self, request, product_id):
        
        product = get_object_or_404(Product, pk = product_id)
            
        data = {
            'title': product.title,
            'article': product.article,
            'price': product.price,
            'barcode': product.barcode,
            'description': product.description,
            'count': product.count,
            'image': product.image,
        } 
           
        return render (request, 'appWarehouse/product.html', data)        
