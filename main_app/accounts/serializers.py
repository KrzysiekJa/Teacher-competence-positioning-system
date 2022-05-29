import emoji
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

try:
    from allauth.utils import email_address_exists
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")




class ValidationSerializer(serializers.Serializer):
    
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError( "A user is already registered with this e-mail address.")
        return email
    
    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    
    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Both password fields didn't match.")
        if emoji.emoji_count(data["password1"]):
            raise serializers.ValidationError("Password can not contain emoji.")
        return data



class UserSerializer(ValidationSerializer):    
    username  = serializers.CharField(required=True, min_length=7, max_length=30)
    email     = serializers.EmailField(required=True, min_length=7, max_length=30)
    password1 = serializers.CharField(write_only=True, min_length=7, max_length=30, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, min_length=7, max_length=30, style={"input_type": "password"})
    
    
    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
        }
    
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        
        return user



class AdminSerializer(ValidationSerializer):    
    username  = serializers.CharField(required=True, min_length=7, max_length=30)
    email     = serializers.EmailField(required=True, min_length=7, max_length=30)
    password1 = serializers.CharField(write_only=True, min_length=7, max_length=30, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, min_length=7, max_length=30, style={"input_type": "password"})
    is_superuser = serializers.BooleanField(default=True)
    
    
    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "is_superuser": self.validated_data.get("is_superuser", ""),
        }
    
    
    def save(self, request):
        adapter = get_adapter()
        admin = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        admin.is_staff = True
        admin.is_admin = True
        admin.is_superuser = True
        adapter.save_user(request, admin, self)
        setup_user_email(request, admin, [])
        
        return admin

