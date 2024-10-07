from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView

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
                 
def books_list(request):
   data = {}
   data["books"] =   Book.objects.all()
   print(data['books'])
   return render(request, 
                 'bookslist.html',
                 data
                 )



class BooksList(ListView):
   queryset = Book.objects.all()
   template_name = 'bookslist.html'
   context_object_name = "books"
   # paginate_by = 4  ПАГИНАЦИЯ
   

class BookDetail(DetailView):
   model = Book
   template_name = 'book_detail.html'
   context_object_name = "book"

class AuthorList(ListView):
   queryset = Author.objects.all()
   template_name = 'author_list.html'
   context_object_name = "authors"
   
class GenreList(ListView):
   queryset = Genre.objects.all()
   template_name = 'genre_list.html'
   context_object_name = "genres"
   