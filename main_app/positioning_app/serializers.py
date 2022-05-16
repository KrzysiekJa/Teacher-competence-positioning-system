from rest_framework import serializers
from .models.Assessment import Assessment
from .models.Institution import Institution
from .models.Tutor import Tutor



class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['user_id', 'tutor_id', 'content', 'grade', 'last_edition_date']
        # excluded 'creation_date'


class AssessmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['user_id', 'tutor_id', 'content', 'grade', 'last_edition_date']
        # excluded 'creation_date'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        exclude = ['creation_date']


class TutorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        exclude = ['creation_date']


class InstitutionSerializer(serializers.ModelSerializer):
    tutors = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all(), many=True, required=False)
    
    class Meta:
        model = Institution
        exclude = ['creation_date']


class InstitutionDetailSerializer(serializers.ModelSerializer):
    tutors = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all(), many=True, required=False)
    
    class Meta:
        model = Institution
        exclude = ['creation_date']


