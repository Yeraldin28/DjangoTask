from django.db import models
from task.models.request_task import RequestTask

class TaskComment(models.Model):
    blog = models.ForeignKey(RequestTask, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.description)