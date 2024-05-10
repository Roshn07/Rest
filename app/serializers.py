from rest_framework import serializers
from .models import students
from django.contrib.auth.models import User



class usersSearilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']


class studentsSerializers(serializers.ModelSerializer):
    user=usersSearilizers()
    class Meta:
        model = students
        fields = '__all__'

