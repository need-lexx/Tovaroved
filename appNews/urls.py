from django.urls import path
from . import views



urlpatterns = [
    path('<int:news_id>', views.show_new, name="urlNews"),  
    path(' ', views.Show_news.as_view(), name="urlAll_news"),  
]