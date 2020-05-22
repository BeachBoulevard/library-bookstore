from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views.generic import ListView, DetailView

from books.models import Book, Author, BookInstance, Class
import datetime
from management.forms import BookRenewalForm

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

def book_renewal(request, pk):
  book_instance = get_object_or_404(BookInstance, pk=pk)

  if request.method == 'POST':
    form = BookRenewalForm(request.POST)

    if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('borrowed_list') )

  else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = BookRenewalForm(initial={'renewal_date': proposed_renewal_date})

  context = {
        'form': form,
        'book_instance': book_instance,
    }

  return render(request, 'management/book_renewal.html', context)

