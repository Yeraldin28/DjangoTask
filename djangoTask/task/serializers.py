from rest_framework import serializers
from .models import Task, TaskComment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_name', 'task_description', 'deadline')
       # read_only_fields = ('created') #no deja que se mopdifique
       
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('description', 'comment_date', 'blog')
       
        