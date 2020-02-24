from django.shortcuts import render
from django.http import HttpResponse
from fourth_third_app.models import User

# Create your views here.

def fourth_third_index(request):
    user = User.objects.order_by('firstname')
    dic = {'user':user}
    return render(request,'fourth_third_app/index.html', context=dic)
