from django.urls import path 
from acb.views import *
urlpatterns = [
    path('country/',country,name='country'),
    
]
