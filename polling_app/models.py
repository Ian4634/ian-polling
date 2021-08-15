from django.db import models

# Create your models here.


class Polls(models.Model):
    owner = models.CharField(max_length=200, default='nobody')
    name = models.CharField(max_length=200)
    questions = models.CharField(max_length=200, default=None)
    answer = models.CharField(max_length=1000, default='')
