from django.contrib.auth.models import User, Group
from rest_framework import serializers
from dashboard_detail.models import customerLog

class customerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = customerLog
        fields = '__all__'