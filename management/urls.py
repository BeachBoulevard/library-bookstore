from django.urls import path

from .views import BorrowedListView, BookListView
from . import views


urlpatterns = [
    path('', BookListView.as_view(), name='management'),
    path('borrowed/', BorrowedListView.as_view(), name='borrowed_list'),
]

#url for renewal
urlpatterns += [
    path('<uuid:pk>/renew/', views.book_renewal, name='book_renewal'),
]