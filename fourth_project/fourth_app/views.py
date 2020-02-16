from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    dict = {'insert_me':'this is views.py file'}
    return render(request,'fourth_app/index.html',context=dict)
