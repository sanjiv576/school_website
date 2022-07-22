from django.urls import path
from customer import views

urlpatterns = [
        path('appointment', views.appointment),
        
]