from rest_framework import serializers
from .models import Task


class TaskSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_name', 'progress')
