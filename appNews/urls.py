from django.urls import path
from . import views



urlpatterns = [
    path('<int:news_id>', views.show_news, name="urlNews"),  
]