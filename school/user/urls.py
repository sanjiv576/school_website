from django.urls import path
from user import views

urlpatterns = [
        path('admin', views.adminPanel),
        path('addNotice', views.addNotice),
        path('addIntro', views.addIntro),
]