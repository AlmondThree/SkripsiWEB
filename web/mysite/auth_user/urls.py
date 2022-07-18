from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginUser', views.loginUser, name='loginUsr'),
    path('logout/', views.logout, name='logout')
    # path('regisAccount/', views.customerRegis, name='regis1')
]