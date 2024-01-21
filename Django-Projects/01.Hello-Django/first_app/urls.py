from django.urls import path
from . import views

urlpatterns =[
    path("hello/",views.say_hello),
    path("template/",views.temp_hello)
]