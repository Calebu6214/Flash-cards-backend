from django.shortcuts import render
from .models import Subject
from .serializer import SubjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class SubjectList(APIView):
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