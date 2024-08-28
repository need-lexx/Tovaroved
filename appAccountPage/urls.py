from django.urls import path
from . import views

urlpatterns = [  
    path('', views.PersonAccount.as_view(), name="urlPersonalAccount"),  
]