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
    path('assessments/', AssessmentListView.as_view(), name='assessment-list'),
    path('assessments/<int:id>', AssessmentDetailView.as_view(), name='assessment-deatail'),
    path('institutions/', InstitutionListView.as_view(), name='institution-list'),
    path('institutions/<int:id>', InstitutionDetailView.as_view(), name='institution-deatail'),
    path('tutors/', TutorListView.as_view(), name='tutor-list'),
    path('tutors/<int:id>', TutorDetailView.as_view(), name='tutor-deatail'),
]

