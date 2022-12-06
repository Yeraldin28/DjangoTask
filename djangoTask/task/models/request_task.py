from django.db import models

from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.
    

class RequestTask(models.Model):
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
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE, null=True, blank=True)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICE, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.task_name)

    #def __call__(self, deadline):
    #deadline debe ser mayor a la fecha de creacion 
    #if deadline <= datetime.now():
        #message= 'La fecha no puede ser menor al dia de creación'
        #raise serializers.ValidationError(message)


    

    



