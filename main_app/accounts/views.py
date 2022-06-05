from .serializers import UserSerializer , AdminSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class UserRegistrationView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    
    def get(self, request, format=None):
        snippet = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdminRegistrationView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    
    def get(self, request, format=None):
        snippet = User.objects.filter(is_superuser=True)
        serializer = AdminSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

