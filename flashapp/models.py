from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    description = models.TextField()
    

    # def __str__(self):
    #     return self.subject
    
    # def save_subject(self):
    #     self.save()

    
    # @classmethod
    # def get_subject_by_id(cls,id):
    #     subject = cls.objects.get(id=id)
    #     return subject

    # @classmethod
    # def get_subject(cls,id):
    #     subject = cls.objects.get(pk=id)
    #     return subject

    # @classmethod
    # def delete_subject(cls,id):
    #     cls.objects.filter(id).delete()

    # @classmethod
    # def display_subject(cls):
    #     subject = cls.objects.all()
    #     return subject

    # @classmethod
    # def update_subject(cls,id,new_update):
    #     cls.objects.filter(id=id).update(subject=new_update)