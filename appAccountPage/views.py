from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest

class PersonAccount (View):
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated and request.user.is_active:
           return super().dispatch(request, *args, **kwargs)
        return redirect('urlPageHome')
    def get(self, request):
        return render(request, 'appAccountPage/index.html')
