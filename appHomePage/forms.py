from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'login__input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'login__input'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'login__input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'login__input'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'login__input'}))
    usable_password = None
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2'] 
        
       
        