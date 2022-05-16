from django.db import models
from django.utils import timezone


class Tutor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    reserach_domain_1 = models.CharField(max_length=40)
    reserach_domain_2 = models.CharField(max_length=40, null=True, blank= True)
    reserach_domain_3 = models.CharField(max_length=40, null=True, blank= True)
    creation_date = models.DateTimeField(default=timezone.now)
    last_edition_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=200, null=True, blank= True)
    nacionality = models.CharField(max_length=50, null=True, blank= True)
    
    def __str__(self):
        return self.name + self.surname
