from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def contact(request):
    return HttpResponse("contact us")

def about(request):
    return HttpResponse("about us")

