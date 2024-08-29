from django.contrib import admin
from .models import News
from django_summernote.admin import SummernoteModelAdmin


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    list_display = ["id", "title", "dtime", "status"]
    list_display_links = ["id", "title", "dtime"]  
    list_filter = ['dtime', 'status']
    search_fields = ["title"]
    summernote_fields = ["desc"]
