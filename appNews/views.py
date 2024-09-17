from django.shortcuts import render, get_object_or_404
from appNews.models import News
from django.http import HttpResponse

    
def show_news (request, news_id):
    new = get_object_or_404(News, pk = news_id)       
    data = {
        'title': new.title,
        'desc': new.desc,
        'dtime': new.dtime,
    }    
    return render (request, 'appNews/index.html', data)      