from django.http.response import Http404
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .models import Subject
from .serializer import SubjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
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
        subject = self.get_subject(pk)
        serializers = SubjectSerializer(subject)
        return Response(serializers.data)