from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .utils import method_permission_classes
from ..models.Institution import Institution
from ..serializers import (
    InstitutionSerializer, 
    InstitutionDetailSerializer
    )



class InstitutionListView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class InstitutionPostView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser]

    def post(self, request, format=None):
        serializer = InstitutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InstitutionDetailView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser]

    def get_object(self, id):
        try:
            return Institution.objects.get(id=id)
        except Institution.DoesNotExist:
            raise Http404

    @method_permission_classes([IsAuthenticatedOrReadOnly])
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = InstitutionDetailSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = InstitutionDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['last_edition_date'] = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


