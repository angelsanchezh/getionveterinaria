from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("bienevenido a mi app")

