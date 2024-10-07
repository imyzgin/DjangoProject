from django.urls import path
from . import views



urlpatterns = [
    path('', views.print_hello),
    # path('books/', views.books_list),
    path("books/", views.BooksList.as_view()),
    path("books/<int:pk>", views.BookDetail.as_view()),
    path("authors/", views.AuthorList.as_view()),
    path("genres/", views.GenreList.as_view(), name="genres"),

    
]