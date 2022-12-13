from django.db import models

from datetime import date
from django.template.defaultfilters import slugify
import datetime
from django.utils import timezone

# Create your models here.
    

class RequestTask(models.Model):
    PRIORITY_CHOICE = (
        ('ALTA', 'ALTA'),
        ('MEDIA', 'MEDIA'),
        ('BAJA', 'BAJA'),
    )
    STATUS_CHOICE = (
        ('BACKLOG', 'BACKLOG'),
        ('TO DO', 'TO DO'),
        ('DOING', 'DOING'),
        ('TEST', 'TEST'),
        ('DONE', 'DONE'),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE, null=True, blank=True,  default='BACKLOG')
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICE, null=True, blank=True, default='BAJA')
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
    def was_published_recenrly(self):
        # al poner la fecha de entrega menor al dia de crewacion debe aparecer en falso 
        return timezone.now() >= self.deadline >= timezone.now() - datetime.timedelta(days=1)
    #def __call__(self, deadline):
    #deadline debe ser mayor a la fecha de creacion 
    #if deadline <= datetime.now():
        #message= 'La fecha no puede ser menor al dia de creación'
        #raise serializers.ValidationError(message)


    

    



