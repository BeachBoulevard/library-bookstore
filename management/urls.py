from django.urls import path

from .views import BorrowedListView, BookListView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('borrowed/', BorrowedListView.as_view(), name='borrowed_list'),
]