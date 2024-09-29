from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecSupport.as_view(), name='urlRecSupport'),
]

