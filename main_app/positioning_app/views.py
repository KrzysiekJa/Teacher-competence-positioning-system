from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.Tutor import Tutor
from .models.Assessment import Assessment
from .models.Institution import Institution
from .serializers import (
    TutorSerializer, 
    TutorDetailSerializer
    )



def index(request):
    if request.method == 'GET':
        return HttpResponse('<h2> View!? </h2>')
    
    if request.method == 'POST':
        return HttpResponse('<h2> Post?! </h2>')


class TutorListView(APIView):
    
    def get(self, request):
        tutor = Tutor.objects.all()
        serializer = TutorSerializer(tutor, many=True)
        return Response(serializer.data)

    def post(self, request):
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
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = TutorDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



