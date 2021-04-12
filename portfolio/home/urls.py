from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('main/', views.main, name='main'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('postSite/', views.postSite),
    path('logout/', views.logout_view, name='logout'),
]