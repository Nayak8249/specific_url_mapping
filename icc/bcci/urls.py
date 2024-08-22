from django.urls import path
from bcci.views import * 
urlpatterns = [
    path('country/',country,name='country'),
    
]
