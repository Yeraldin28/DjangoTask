from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from task.models.request_task import RequestTask
from task.models.request_comment import TaskComment
from task.serializers.serializers import ProjectSerializer, CommentSerializer






class ProjectViewSet(viewsets.ModelViewSet):
    queryset = RequestTask.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class ProjectViewComment(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
class TaskViewSet(viewsets.ModelViewSet):
    
    queryset  = RequestTask.objects.all()
    serializer_class = ProjectSerializer
    