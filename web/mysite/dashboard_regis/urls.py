from django.urls import path

from . import views

urlpatterns = [
    path('regis/', views.home, name='regis'),
    path('regisAccount/', views.customerRegis, name='regis1')
]