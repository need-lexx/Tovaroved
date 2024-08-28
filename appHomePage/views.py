from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class LogoutAccount(View):
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated and request.user.is_active:
           return super().dispatch(request, *args, **kwargs)
        return redirect('urlPageHome')
    
    def get(self, request):
        logout(request)
        return ('urlPageHome')
    
class AuthPage(View):
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('urlPersonalAccount')
    def get(self, request):       
        return render(request, 'appHomePage/authorization/index.html')
    def post(self, request):   
        username = request.POST['login']    
        password = request.POST['password'] 

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:              #пользователь активный для авторизации
               login(request, user) 

            return JsonResponse({
                'status': 'success',            
            })
        
        return JsonResponse({
            'status': 'error',            
        })
        

class RegPage(View):
    def get(self, request):       
        return render(request, 'appHomePage/registration/index.html')
    
    def post(self, request):   
        username = request.POST['username']    
        password = request.POST['password'] 
        
        User.objects.create(
            username=username,
            password=make_password(password)
        ) 
        return JsonResponse({
             'status': 'success',           
        })
        
        
        
        
