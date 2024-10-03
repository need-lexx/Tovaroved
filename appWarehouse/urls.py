from django.urls import path
from . import views


urlpatterns = [   
    path('add_product/', views.AddProduct.as_view(), name='urlAddProduct'),
    path('add_warehouse/', views.AddWarehouse.as_view(), name='urlAddWarehouse'),
    path('<int:pk>/edit', views.ChangeData.as_view(), name='urlChangeData'),
    path('<int:pk>/delete', views.DeleteProduct.as_view(), name='urlDeleteProduct'),
    path('<int:pk>', views.product, name='urlProduct'),
    path('', views.PersonAccount.as_view(), name="urlPersonalAccount"),      
]



