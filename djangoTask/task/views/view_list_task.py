from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from task.models.request_task import RequestTask
from task.models.request_comment import TaskComment
from task.serializers.serializers import ProjectSerializer, CommentSerializer




#listar el proyecto
class ProjectList(generics.ListAPIView):
    queryset = RequestTask.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend
    ]
    search_fields = ('name', 'status')
    ordering_fields = ('name',)
    ordering = ('name',)
