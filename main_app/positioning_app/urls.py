from django.urls import path
from .views.AssessmentViews import (
    AssessmentListView, 
    AssessmentPostView,
    AssessmentDetailView
    )
from .views.InstitutionViews import (
    InstitutionListView, 
    InstitutionPostView,
    InstitutionDetailView
    )
from .views.TutorViews import (
    TutorListView, 
    TutorPostView,
    TutorDetailView
    )



urlpatterns = [
    path('assessments', AssessmentListView.as_view(), name='assessment-list'),
    path('assessments/post', AssessmentPostView.as_view(), name='assessment-post'),
    path('assessments/<int:id>', AssessmentDetailView.as_view(), name='assessment-deatail'),
    path('institutions', InstitutionListView.as_view(), name='institution-list'),
    path('institutions/post', InstitutionPostView.as_view(), name='institution-post'),
    path('institutions/<int:id>', InstitutionDetailView.as_view(), name='institution-deatail'),
    path('tutors', TutorListView.as_view(), name='tutor-list'),
    path('tutors/post', TutorPostView.as_view(), name='tutor-post'),
    path('tutors/<int:id>', TutorDetailView.as_view(), name='tutor-deatail'),
]

