from rest_framework import serializers
from task.models.request_task import RequestTask
from task.models.request_comment import TaskComment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTask
        fields = ('name', 'description', 'status','priority', 'deadline')
        # read_only_fields = ('created') #no deja que se mopdifique



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('description', 'blog')


