from django.http import request
from django.shortcuts import render

# Create your views here.

def corona(request):
    return render(request,'corona.html')

def Bootstrap(request):
    return render(request,'Bootstrap.html')