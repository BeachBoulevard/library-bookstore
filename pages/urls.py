from django.urls import path
from .views import HomePageView, AboutPageView, BycategoryPageView

urlpatterns = [
  path('about/', AboutPageView.as_view(), name='about'),
  path('bycategory/', BycategoryPageView.as_view(), name='bycategory'),
  path('', HomePageView.as_view(), name='home'),

]