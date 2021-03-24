# pages/urls.py
from django.urls import path

from .views import HomePageView,AboutUsView,ContactUsView, RegisterView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('aboutus/', AboutUsView.as_view() , name='aboutus'),
    path('contactus/', ContactUsView.as_view() , name='contactus'),
    path('register/', RegisterView.as_view() , name='register'),
]