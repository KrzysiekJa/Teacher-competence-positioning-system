from django.urls import path
from .views.AssessmentViews import (
    AssessmentListView, 
    AssessmentDetailView
    )
from .views.InstitutionViews import (
    InstitutionListView, 
    InstitutionDetailView
    )
from .views.TutorViews import (
    index, 
    TutorListView, 
    TutorDetailView
    )



urlpatterns = [
    path('', index),
    path('assessment/', AssessmentListView.as_view(), name='assessment-list'),
    path('assessment/<int:id>', AssessmentDetailView.as_view(), name='assessment-deatail'),
    path('institution/', InstitutionListView.as_view(), name='institution-list'),
    path('institution/<int:id>', InstitutionDetailView.as_view(), name='institution-deatail'),
    path('tutor/', TutorListView.as_view(), name='tutor-list'),
    path('tutor/<int:id>', TutorDetailView.as_view(), name='tutor-deatail'),
]

