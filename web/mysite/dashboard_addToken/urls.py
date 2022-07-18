from django.urls import path

from . import views

urlpatterns = [
    path('addToken/', views.addToken, name='addToken'),
    path('addToken/<paramId>', views.addToken, name='addToken')
]