from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views.generic import ListView, DetailView

from books.models import Book, Author, BookInstance, Class


class BookListView(ListView):
  model = Book
  context_object_name = 'book_list'
  template_name = 'management/management_home.html'


class BorrowedListView(ListView):
  model = BookInstance
  context_object_name = 'borrowed_list'
  template_name = 'management/borrowed_list.html'
  
  def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

