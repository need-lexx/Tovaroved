from django.contrib import admin
from .models import News
from django_summernote.admin import SummernoteModelAdmin
from unfold.admin import ModelAdmin

@admin.register(News)
class NewsAdmin(ModelAdmin, SummernoteModelAdmin):
    list_display = ["id", "title", "dtime", "status"]
    list_display_links = ["id", "title", "dtime"]  
    list_filter = ['dtime', 'status']
    search_fields = ["title"]
    summernote_fields = ["desc"]
