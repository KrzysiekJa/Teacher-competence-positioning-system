from .serializers import UserSerializer , AdminSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny



class UserRegistrationView(APIView):
    
    permission_classes = [AllowAny]
    
    def get(self, request, format=None):
        snippet = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user  = serializer.save(request)
            token = Token.objects.create(user=user)
            data['username'] = user.username
            data['email'] = user.email
            data['token'] = token.key
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdminRegistrationView(APIView):
    
    permission_classes = [AllowAny]
    
    def get(self, request, format=None):
        snippet = User.objects.filter(is_superuser=True)
        serializer = AdminSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            admin = serializer.save(request)
            token = Token.objects.create(user=admin)
            data['username'] = admin.username
            data['email'] = admin.email
            data['token'] = token.key
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

