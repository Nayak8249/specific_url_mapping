from django.urls import path 
from pcb.views import *
urlpatterns = [
    path('country/',country,name='country'),
    
]
