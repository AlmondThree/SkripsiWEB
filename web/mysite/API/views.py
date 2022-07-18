from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from API.serializers import customerLogSerializer
from dashboard_detail.models import customerLog

# Create your views here.
def not_found(request):
    return HttpResponse("Page not found")

def dataAPI(request):
    return HttpResponse("data API")

class customerLogViewSet(viewsets.ModelViewSet):
    queryset = customerLog.objects.all()
    serializer_class = customerLogSerializer