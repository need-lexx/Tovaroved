from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse_lazy

from .forms import LoginUserForm, RegisterUserForm
from appNews.models import News


class AuthPage(LoginView, ListView):                
    model = News
    
    template_name = 'appHomePage/authorization/index.html'    
    form_class = LoginUserForm                
    
    context_object_name = 'news'
    ordering = ['-dtime']
    
class LogoutAccount(View):
    def get(self, request):
        logout(request)
        return redirect('urlPageHome')

class RegPage(CreateView):       
    template_name = 'appHomePage/registration/index.html'    
    form_class = RegisterUserForm 
    success_url =  reverse_lazy('urlPageHome')
    
    
  


