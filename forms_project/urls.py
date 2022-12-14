from django.contrib import admin
from django.urls import path
from forms_app import views

urlpatterns = [
    path('', views.index),
    path('postuser/', views.postuser)
]
