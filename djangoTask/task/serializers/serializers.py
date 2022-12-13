from rest_framework import serializers
from task.models.request_task import RequestTask
from task.models.request_comment import TaskComment
from django.utils import timezone
import datetime


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTask
        fields = ('id','name', 'description', 'status','priority', 'deadline')
        # read_only_fields = ('created') #no deja que se mopdifique
    def was_published_recenrly(self):
        # al poner la fecha de entrega menor al dia de crewacion debe aparecer en falso 
        return timezone.now() >= self.deadline >= timezone.now() - datetime.timedelta(days=1)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('description', 'blog')



