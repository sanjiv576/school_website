from django.urls import path
from home import views

urlpatterns = [
        path('', views.index),
        path('/register', views.register, name="register"),
        path('/home', views.home, name="home"),
]