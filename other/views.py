from django.shortcuts import render
from datetime import datetime
from django.views import View
from django.http import HttpResponse
from random import random

# Create your views here.
class CurrentDateView(View):

    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)

class RandomNumView(View):
    def get(self, request):
        some_num = random()
        return HttpResponse(some_num)

class HelloView(View):
    def get(self, request):
        _str = "<h1>Hello from Django</h1>"
        return HttpResponse(_str)

class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')
