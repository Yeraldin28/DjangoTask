from django.db import models

from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.
    

class Task(models.Model):
    STATUS_CHOICE = (
        ('ALTA', 'ALTA'),
        ('MEDIA', 'MEDIA'),
        ('BAJA', 'BAJA'),
    )
    PRIORITY_CHOICE = (
        ('BACKLOG', 'BACKLOG'),
        ('TO DO', 'TO DO'),
        ('DOING', 'DOING'),
        ('TEST', 'TEST'),
        ('DONE', 'DONE'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICE)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICE)
    deadline = models.DateField()

    def __str__(self):
        return str(self.name)

    def __call__(self, deadline):
    #deadline debe ser mayor a la fecha de creacion 
    if deadline <= datetime.now():
        message= 'La fecha no puede ser menor al dia de creación'
        raise serializers.ValidationError(message)

class TaskComment(models.Model):
    description = models.TextField()
    blog = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)
    

    



