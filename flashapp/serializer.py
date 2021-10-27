from rest_framework import serializers
from .models import Subject
from django.contrib.auth.models import User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=('id','title','subject', 'description')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','is_staff']