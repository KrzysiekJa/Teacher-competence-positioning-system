from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tutor', views.TutorListView.as_view(), name='tutor')
]
