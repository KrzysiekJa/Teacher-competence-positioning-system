from django.urls import path
from .views import (
    index, 
    TutorListView, 
    TutorDetailView
    )

urlpatterns = [
    path('', index),
    path('tutor/', TutorListView.as_view(), name='tutor-list'),
    path('tutor/<int:id>', TutorDetailView.as_view(), name='tutor-deatail'),
]

