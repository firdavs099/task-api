from rest_framework import generics
from django.shortcuts import render
from .models import Task
from .serialiser import TaskSerialiser


# Create your views here

class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
