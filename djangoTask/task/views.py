from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Task, TaskComment
from .serializers import ProjectSerializer, CommentSerializer

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset  = Task.objects.all()
    serializer_class = ProjectSerializer