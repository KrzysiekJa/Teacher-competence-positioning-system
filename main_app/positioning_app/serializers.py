from rest_framework import serializers
from .models.Tutor import Tutor
from .models.Assessment import Assessment
from .models.Institution import Institution



class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class TutorDetailSerializer(serializers.ModelSerializer):
    pass
    
