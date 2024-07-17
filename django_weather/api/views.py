from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def empty_api(request):
    return HttpResponse('<h1>API is not ready :(</h1>')