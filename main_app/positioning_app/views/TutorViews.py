from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .utils import method_permission_classes
from ..models.Tutor import Tutor
from ..serializers import (
    TutorSerializer, 
    TutorDetailSerializer
    )



class TutorListView(APIView):
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes     = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class TutorPostView(APIView):
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes     = [IsAdminUser]
    
    def post(self, request, format=None):
        serializer = TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TutorDetailView(APIView):
    
    #authentication_classes = [TokenAuthentication]
    #permission_classes     = [IsAdminUser]

    def get_object(self, id):
        try:
            return Tutor.objects.get(id=id)
        except Tutor.DoesNotExist:
            raise Http404

    #@method_permission_classes([IsAuthenticatedOrReadOnly])
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = TutorDetailSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = TutorDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['last_edition_date'] = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


