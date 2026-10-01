from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index_view(request):
    
    return render(request, 'website/index.html')

def about_view(request):
    return HttpResponse("<h1>This is contact us</h1>")

def contactUs_view(request):
    return HttpResponse("")
