from .models import Task, TaskComment
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, CommentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
   queryset = Task.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = ProjectSerializer
   
class ProjectViewComment(viewsets.ModelViewSet):
   queryset = TaskComment.objects.all()
   permission_classes = [permissions.AllowAny]
   serializer_class = CommentSerializer
    
