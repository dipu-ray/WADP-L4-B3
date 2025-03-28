from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    department=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.email)
        instance.department = validated_data.get('department', instance.content)
        instance.email = validated_data.get('email', instance.created)
        instance.save()
        return instance
