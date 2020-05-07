from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # connecting to home page view
    path('about/', views.about, name='blog-about'),
] 
