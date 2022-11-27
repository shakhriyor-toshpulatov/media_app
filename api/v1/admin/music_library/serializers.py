from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from music_library.models import *


class AdminLicenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = [
            'id',
            'user',
            'text',
        ]


class AdminLicenseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = [
            'id',
            'user',
            'text',
        ]


class AdminLicenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = [
            'id',
            'user',
            'text',
        ]

    def to_representation(self, instance: License):
        response = super().to_representation(instance)
        response['user'] = instance.user.username
        response['first_name'] = instance.user.first_name
        response['Last_name'] = instance.user.last_name
        return response


class AdminLicenseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = [
            'id',
            'user',
            'text',
        ]
