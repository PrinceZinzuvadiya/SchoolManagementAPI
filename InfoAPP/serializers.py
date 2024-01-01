from rest_framework import serializers
from .models import faculty, student

class facultyserializers(serializers.ModelSerializer):
    class Meta:
        model=faculty
        fields='__all__'

class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
        
