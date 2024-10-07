from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def print_hello(request): 
   # return HttpResponse("Hello world!")
   return render(request, 
                 'index.html',
                 context = {
                    'books': Book.objects.all(),
                    'authors': Author.objects.all(),
                    'genres': Genre.objects.all()
                 })
                 
