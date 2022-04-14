from django.urls import path, include
from .views import UserRegisterView, AdminRegisterView

urlpatterns = [
    #url(r'^rest-auth/', include('rest_auth.urls')),
    path("register/", UserRegisterView.as_view(), name='user_register'),
    #path('register/<int:pk>/', UserRegisterView.as_view()),
    path("admin/", AdminRegisterView.as_view(), name='admin_register'),
]
