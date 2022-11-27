import json
import re
from django.contrib.auth import login
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer as TokenSerializer

from user.models import UserRoleChoices, User
import logging

logger = logging.getLogger(__name__)


class RefreshTokenSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_role"] = user.role
        return token


class TokenObtainPairSerializer(TokenSerializer):
    def get_token(self, user):
        sent_role = self.context.get('request').data.get('role')
        token = super().get_token(user)
        token["user_role"] = user.role
        token["last_name"] = user.last_name
        token["first_name"] = user.first_name
        token["username"] = user.username
        token["sent_role"] = sent_role
        return token

    def validate(self, attr):
        sent_role = self.context.get('request').data.get('role')
        if sent_role not in UserRoleChoices.values:
            raise PermissionDenied('sent role is not correct')
        return super().validate(attr)
