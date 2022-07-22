
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    # path('register/', include('home.urls')),
    path('home/', include('home.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('user/', include('user.urls')),
    path('customer/', include('customer.urls')),
    
]
