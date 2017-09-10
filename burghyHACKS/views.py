from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    temp = loader.get_template("index.html")
    return HttpResponse(temp.render())