from rest_framework import serializers
from music_library.models import *


# ------------------------License-------------------------------
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


# ------------------------Album-------------------------------
class AdminAlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'user',
            'name',
            'description',
            'private',
            'cover'
        ]


class AdminAlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'user',
            'name',
            'private',
            'cover'
        ]


class AdminAlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'user',
            'name',
            'description',
            'private',
            'cover'
        ]


class AdminAlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id',
            'user',
            'name',
            'description',
            'private',
            'cover'
        ]
