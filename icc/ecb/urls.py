from django.urls import path 
from ecb.views import *
urlpatterns = [
    path('country/',country,name='country'),
    
]
