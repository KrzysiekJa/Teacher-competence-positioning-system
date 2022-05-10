from rest_framework import serializers
from .models.Assessment import Assessment
from .models.Institution import Institution
from .models.Tutor import Tutor



class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'


class AssessmentDetailSerializer(serializers.ModelSerializer):
    pass
    

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class InstitutionDetailSerializer(serializers.ModelSerializer):
    pass


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class TutorDetailSerializer(serializers.ModelSerializer):
    pass


