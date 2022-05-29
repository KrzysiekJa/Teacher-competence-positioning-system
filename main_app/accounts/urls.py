from django.urls import path, include
from .views import UserRegistrationView, AdminRegistrationView


urlpatterns = [
    path("registration", UserRegistrationView.as_view(), name='user-registration'),
    path("admin", AdminRegistrationView.as_view(), name='admin-registration'),
]
