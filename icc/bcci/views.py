from django.shortcuts import render
from django.http import HttpResponse

def country(request):
    return HttpResponse('<h1> india  has the largect networth cricket board in the world </h1> ')