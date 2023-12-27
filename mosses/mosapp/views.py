from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
from django.http import HttpResponse

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def home(request):
    return HttpResponse("Welcome to Mosses Project, Nothing here, use it on the terminul ;)")
