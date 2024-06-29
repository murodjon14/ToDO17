from django.db import models
from user.models import *

class Plan(models.Model):
    nom = models.CharField(max_length=255)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    deadline =models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
