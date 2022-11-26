from django.contrib.auth import login
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer


class RefreshTokenSerializer(TokenRefreshSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_role"] = user.role
        return token


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)
        token["last_name"] = user.last_name
        token["first_name"] = user.first_name
        token["username"] = user.username
        return token
