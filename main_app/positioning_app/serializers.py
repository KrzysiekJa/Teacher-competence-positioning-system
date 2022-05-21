from rest_framework import serializers
from .models.Assessment import Assessment
from .models.Institution import Institution
from .models.Tutor import Tutor



### ----- Assessment ----- ###
class AssessmentListSerializer(serializers.ListSerializer):
    pass


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        list_serializer_class = AssessmentListSerializer
        fields = ['id', 'user_id', 'tutor_id', 'content', 'grade', 'last_edition_date']
        # excluded 'creation_date'


class AssessmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'user_id', 'tutor_id', 'content', 'grade', 'last_edition_date']
        # excluded 'creation_date'


### ----- Tutor ----- ###
class TutorListSerializer(serializers.ListSerializer):
    pass


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        list_serializer_class = TutorListSerializer
        exclude = ['creation_date']


class TutorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        exclude = ['creation_date']


### ----- Institution ----- ###
class InstitutionListSerializer(serializers.ListSerializer):
    pass


class InstitutionSerializer(serializers.ModelSerializer):
    tutors = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all(), many=True, required=False)
    
    class Meta:
        model = Institution
        list_serializer_class = InstitutionListSerializer
        exclude = ['creation_date']


class InstitutionDetailSerializer(serializers.ModelSerializer):
    tutors = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all(), many=True, required=False)
    
    class Meta:
        model = Institution
        exclude = ['creation_date']


