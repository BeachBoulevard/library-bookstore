from django.urls import path

from .views import BorrowedListView, ManagementBookListView,ManagementBookDetailView, ManagementSearchResultsListView, ManagementHomePageView
from . import views


urlpatterns = [
    path('', ManagementHomePageView.as_view(), name='management_home'),
    path('<uuid:pk>', ManagementBookDetailView.as_view(), name='management_book_detail'),
    path('books/', ManagementBookListView.as_view(), name='book_list'),
    path('borrowed/', BorrowedListView.as_view(), name='borrowed_list'),
    path('search/', ManagementSearchResultsListView.as_view(), name='management_search_results'),
]

#url for renewal
urlpatterns += [
    path('<uuid:pk>/renew/', views.book_renewal, name='book_renewal'),    
]

#url for crud actions on books
urlpatterns += [  
    path('create/', views.BookCreate.as_view(), name='book_create'),
    path('<uuid:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('<uuid:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]