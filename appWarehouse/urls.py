from django.urls import path
from . import views

urlpatterns = [   
    path('addproduct/', views.addProduct, name='urlAddProduct'),
    path('addwarehouse/', views.AddWarehouse.as_view(), name='urlAddWarehouse'),
    path('', views.PersonAccount.as_view(), name="urlPersonalAccount"),
      
]

