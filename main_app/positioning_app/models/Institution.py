from django.db import models
from django.utils import timezone
from .Tutor import Tutor


class Institution(models.Model):
    name = models.CharField(max_length=100, unique=True, default='noname-institution')
    address = models.CharField(max_length=100, unique=True, null=True)
    extra_information = models.TextField(max_length=200, null=True, blank= True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    profile = models.CharField(max_length=50, null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    last_edition_date = models.DateTimeField(default=timezone.now)
    tutors = models.ManyToManyField(Tutor, related_name='institutions')
    
    def __str__(self):
        return self.name

