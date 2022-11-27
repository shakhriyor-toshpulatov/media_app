from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from user.models import User


class AdminUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'role',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'phone_number'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        try:
            validate_password(value)
            return super().validate(value)
        except ValidationError as validator_error:
            raise validator_error

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class AdminUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'role'
        ]


class AdminUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'role',
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class AdminUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'role',
            'username',
            'first_name',
            'last_name',
            'email',
        ]
