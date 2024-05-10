from rest_framework import serializers
from .models import student,subject

class studentSerializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'


class subjectSearilizers(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields='__all__'