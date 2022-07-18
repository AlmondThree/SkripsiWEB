from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from restAPI.serializers import UserSerializer, GroupSerializer, DataSerializer, customerIdSerializer
from restAPI.models import Data, customerId

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticated]

class customerIdViewSet(viewsets.ModelViewSet):
    queryset = customerId.objects.all()
    serializer_class = customerIdSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]