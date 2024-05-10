from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='Main_page'),
    path('about/', views.about_me, name='About_me'),
]