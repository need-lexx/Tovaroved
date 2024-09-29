from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.LogoutAccount.as_view(), name="urlLogoutAccount"),        
    path('reg/', views.RegPage.as_view(), name="urlRegPage"), 
    path('', views.AuthPage.as_view(), name="urlPageHome"),       
    
    
      
]