from django.urls import path
from . import views

urlpatterns = [   
    path('addproduct/', views.addProduct, name='urlAddProduct'),
    path('addwarehouse/', views.AddWarehouse.as_view(), name='urlAddWarehouse'),
    path('income_product/', views.IncomeProduct.as_view(), name='urlIncomeProduct'),
    path('expense_product/', views.ExpenseProduct.as_view(), name='urlExpenseProduct'),
    path('', views.PersonAccount.as_view(), name="urlPersonalAccount"),
      
]

