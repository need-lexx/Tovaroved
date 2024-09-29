from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AddProductForm, ChangeProductCount
from .models import Product
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.contrib import messages
from .services import increase_count, decrease_count




class PersonAccount (TemplateView):
    template_name = 'appWarehouse/index.html'    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(user=self.request.user)
        context['products'] = products
        return context      
 
        
class AddProduct (CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'appWarehouse/add_product.html'
    success_url = reverse_lazy('urlPersonalAccount')
    
    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)


class AddWarehouse (View):
    def get(self, request):
        return render(request, 'appWarehouse/add_warehouse.html')
    
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ChangeProductCount(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            action = form.cleaned_data['action']
            try:
                if action == 'increase':
                    increase_count(product, quantity)
                elif action == 'decrease':
                    decrease_count(product, quantity)
                else:
                    raise Exception("Неверное значение действия.")
            except ValidationError as err:
                messages.error(request, str(err))
            return redirect('urlPersonalAccount')
    else:
        form = ChangeProductCount()   
        
    return render(request, 'appWarehouse/product.html', {'product': product, 'form': form}) 
    
  
class ChangeData (UpdateView):
     model = Product     
     template_name = 'appWarehouse/change_data.html'
     fields = ['title', 'article', 'price', 'description', 'image']
     
     def get_success_url(self):
             product_id = self.object.id
             return reverse_lazy('urlProduct', kwargs={'pk': product_id})
     
    
    
