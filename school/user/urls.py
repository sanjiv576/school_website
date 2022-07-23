from django.urls import path

from user import views

urlpatterns = [
        path('admin', views.adminPanel),
        path('addNotice', views.addNotice),
        path('addIntro', views.addIntro),
        path('viewNotice', views.viewNotice),
        path('viewCustomer', views.viewCustomer),
        path('viewAppointment', views.viewAppointment),
        path('viewIntro', views.viewIntro),
        path('editNotice/<int:c_id>', views.editNotice),
        path('editIntro/<int:c_id>', views.editIntro),
        path('updateIntro/<int:c_id>', views.updateIntro),
        path('updateNotice/<int:c_id>', views.updateNotice),
        path('deleteIntro/<int:c_id>', views.deleteIntro),
        path('deleteNotice/<int:c_id>', views.deleteNotice),
        path('sortViewCustomer/<str:sortedBy>', views.sortViewCustomer),

]