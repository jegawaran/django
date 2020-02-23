from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index),
    path('fetch_data/', views.fetchData)   
]
