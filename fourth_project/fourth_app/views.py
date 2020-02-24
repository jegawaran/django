from django.shortcuts import render
from django.http import HttpResponse
from fourth_app.models import Topic,AccessRecord,Webpage

# Create your views here.

def index(request):
    # dict = {'insert_me':'Python Django Project','pics':'Python Pictures'}    
    # return render(request,'fourth_app/index.html',context=dict)
    accessRecord = AccessRecord.objects.order_by('date')
    fetch_dict = {'fetchvalue': accessRecord, 'insert_me':'Python + Django','pics':'python/Django' }
    return render(request, 'fourth_app/index.html', context=fetch_dict)


def fetchData(request):
    accessRecord = AccessRecord.objects.order_by('date')
    fetch_dict = {'fetchvalue': accessRecord }
    return render(request, 'fourth_app/fetch.html', context=fetch_dict)