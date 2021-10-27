from django.http.response import Http404
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .models import Subject
from .serializer import SubjectSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from flashapp import models

from flashapp import serializer
# Create your views here.

class SubjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_sub = Subject.objects.all()
        serializers = SubjectSerializer(all_sub, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SubjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_subject(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        subjects = self.get_subject(pk)
        serializers = SubjectSerializer(subjects)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        subjects = self.get_subject(pk)
        serializers = SubjectSerializer(subjects, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subjects = self.get_subject(pk)
        subjects.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(APIView):
    subjects=models.User.objects.all()
    serializer_class=UserSerializer