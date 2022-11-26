from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from . import serializers
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.response import Response


class RefreshTokenView(TokenRefreshView):
    serializer_class = serializers.RefreshTokenSerializer


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = serializers.UserTokenObtainPairSerializer


class APILogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
