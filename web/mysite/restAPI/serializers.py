from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restAPI.models import Data, customerId

class customerIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customerId
        fields = '__all__'

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']