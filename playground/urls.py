#This file is created by Ayush
from django.urls import path
from.import views

#URL Conf
urlpatterns = [
    path('hello/',views.say_hello)
]