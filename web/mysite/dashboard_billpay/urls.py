from django.urls import path

from . import views

urlpatterns = [
    path('billpay/', views.billpay, name='billpay'),
    path('billpay/<paramId>', views.billpay, name='billpay')
]