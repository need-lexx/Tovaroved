from django.shortcuts import render, get_object_or_404
from appNews.models import News
from django.views.generic import ListView


    
def show_new (request, news_id):
    new = get_object_or_404(News, pk = news_id)       
    data = {
        'title': new.title,
        'desc': new.desc,
        'dtime': new.dtime,
    }    
    return render (request, 'appNews/index.html', data)  



class Show_news(ListView):
    model = News    
    template_name = 'appNews/all_news.html' 
    context_object_name = 'news'
    ordering=['-dtime']
    
    




    