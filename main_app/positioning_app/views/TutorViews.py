from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.Tutor import Tutor
from ..serializers import (
    TutorSerializer, 
    TutorDetailSerializer
    )



def index(request):
    if request.method == 'GET':
        return HttpResponse('<h1> Bartek!? </h1>')
    
    if request.method == 'POST':
        return HttpResponse('<h2> Post?! </h2>')



class TutorListView(APIView):
    
    def get(self, request, format=None):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TutorDetailView(APIView):

    def get_object(self, id):
        try:
            return Tutor.objects.get(id=id)
        except Tutor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = TutorDetailSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = TutorDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.data['last_edition_date'] = timezone.now
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


