from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions


from task.models.request_task import RequestTask

from task.serializers.serializers import ProjectSerializer, CommentSerializer

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset  = Task.objects.all()
    serializer_class = ProjectSerializer
