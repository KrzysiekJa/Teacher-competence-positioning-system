from django.db import models
from django.utils import timezone
from .Tutor import Tutor


class Institution(models.Model):
    address = models.CharField(max_length=100)
    extra_information = models.TextField(max_length=200, null=True, blank= True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    profile = models.CharField(max_length=50, null=True, blank= True)
    creation_date = models.DateTimeField(default=timezone.now)
    last_edition_date = models.DateTimeField(default=timezone.now)


class TutorInstitution(models.Model):
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE)