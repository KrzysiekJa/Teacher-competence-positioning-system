from django.urls import path, include
from .views import UserRegistrationView, AdminRegistrationView

urlpatterns = [
    #url(r'^rest-auth/', include('rest_auth.urls')),
    path("registration/", UserRegistrationView.as_view(), name='user-registration'),
    #path('register/<int:pk>/', UserRegisterView.as_view()),
    path("admin/", AdminRegistrationView.as_view(), name='admin-registration'),
]
