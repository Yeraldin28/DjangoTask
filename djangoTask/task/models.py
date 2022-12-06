from django.db import models

from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.
class TaskStatus(models.Model):
    status_name = models.CharField(max_length=200, default="")
    def __str__(self):
        return str(self.status_name)
class TaskPriority(models.Model):
    priority_name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.priority_name)
    
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, null=True)
    priority = models.ForeignKey(TaskPriority, on_delete=models.CASCADE, null=True)
    deadline = models.DateField()
    def __str__(self):
        return str(self.task_name)

class TaskComment(models.Model):
   description = models.TextField()
   blog = models.ForeignKey(Task, on_delete=models.CASCADE)

   def __str__(self):
        return str(self.description)
    

    



