from django.contrib import admin
from django.urls import path
from forms_app import views

urlpatterns = [
    path('', views.index),
    path('postuser/', views.postuser),
    path('second_task', views.main),
    path('order/<name>/<country>/<town>/<street>/<number_house>/<flat>', views.order, name='order')
]
