from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    description = models.TextField()