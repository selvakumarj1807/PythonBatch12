from django.urls import path

from app02 import views


urlpatterns = [
    path('', views.app02_index),
]
