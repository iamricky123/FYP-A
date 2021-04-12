# pages/urls.py
from django.urls import path

from .views import HomePageView,AboutUsView,ContactUsView, RegisterView, ArachniFormView, ArachniRedirectView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('aboutus/', AboutUsView.as_view() , name='aboutus'),
    path('contactus/', ContactUsView.as_view() , name='contactus'),
    path('register/', RegisterView.as_view() , name='register'),
    path('arachni_form/', ArachniFormView.as_view() , name='arachni_form'),
    path('arachni_redirect/', ArachniRedirectView.as_view() , name='arachni_redirect'),
    path ('Userregistration',views.Userregistration),
]