from django.db import models
from django.utils import timezone
from .Tutor import Tutor
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Assessment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    creation_date = models.DateTimeField(default=timezone.now)
    last_edition_date = models.DateTimeField(default=timezone.now)
    