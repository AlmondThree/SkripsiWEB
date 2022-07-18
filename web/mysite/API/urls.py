from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.customerLogViewSet)

urlpatterns = [
    path('', views.not_found, name='not_found'),
    path('/', views.not_found, name='not_found'),
    path('data/', include(router.urls), name='api_data'),
]