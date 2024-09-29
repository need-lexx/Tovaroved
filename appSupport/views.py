from django.views import View
from .models import ReturnRequest
from django.http import JsonResponse
from django.shortcuts import render, redirect


class RecSupport(View):
    def get (self, request):           
        return render (request, 'appSupport/index.html')
                       
    def post(self, request):
        ReturnRequest.objects.create(
            first_name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            comment=request.POST['comment'],
        )
        
        return JsonResponse({
                "status": "success"
        })
    
    
    