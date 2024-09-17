from django.urls import path
from . import views

urlpatterns = [   
    path('add_product/', views.addProduct, name='urlAddProduct'),
    path('add_warehouse/', views.AddWarehouse.as_view(), name='urlAddWarehouse'),
    path('income_product/', views.IncomeProduct.as_view(), name='urlIncomeProduct'),
    path('expense_product/', views.ExpenseProduct.as_view(), name='urlExpenseProduct'),
    path('<int:product_id>', views.ProductPage.as_view(), name='urlProduct'),
    path('', views.PersonAccount.as_view(), name="urlPersonalAccount"),
      
]

