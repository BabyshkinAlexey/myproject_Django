from django.urls import path
from . import views

app_name = 'myapp4'

urlpatterns = [

    path('', views.index, name='index'),  # вывод главной страницы
    path('client/<int:client_id>/', views.client_order, name='client_order'),

]