from django.contrib.admin.models import LogEntry
from rest_framework import serializers
from django.contrib.admin.models import LogEntry
# Create your models here.

class log_history_serializer(serializers.ModelSerializer):

    

    class Meta:
        model = LogEntry
        fields = '__all__'


