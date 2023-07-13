from rest_framework import serializers
from .models import *



class StudentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields='__all__'