from django.urls import path

from . import views

urlpatterns = [
    # path('customer/', views.detail, name='detail'),
    path('customer/<paramId>/', views.detail, name='detail'),
    path('detail/<paramPage>/', views.description, name='Detail description')
]