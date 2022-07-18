from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='index1'),
    path('homeLogin/', views.home_login, name='index2'),
    path('sendContactUs/', views.getContactUs, name='sendMessage')
    #path('test/', views.test, name='test')
]