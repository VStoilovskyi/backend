from django.contrib.auth.models import User
from rest_framework import serializers
from stvadym.restapp.models import Note
from rest_framework.serializers import ValidationError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwards = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'summary', 'description', 'priority', 'userId']
        # filter_backends = (filters.OrderingFilter,)
        # ordering_fields = ('userId')


    def validate_priority(self, value):
        priority = value
        if priority not in ('high', 'medium', 'low'):
            raise ValidationError('Priority should be one of: High, Medium, Low')
        return value


