from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from api.v1.admin.user.serializers import *
from api.v1.permissions import AdminPermission, SingerPermission, ListenerPermission
from user.models import User


# -------------------------------USER------------------------------
class AdminUserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = AdminUserCreateSerializer


class AdminUserListView(ListAPIView):
    permission_classes = [AdminPermission | SingerPermission | ListenerPermission]
    serializer_class = AdminUserListSerializer
    queryset = User.objects.all()


class AdminUserDetailView(RetrieveAPIView):
    permission_classes = [AdminPermission | SingerPermission | ListenerPermission]
    serializer_class = AdminUserDetailSerializer
    queryset = User.objects.all()


class AdminUserUpdateView(UpdateAPIView):
    permission_classes = [AdminPermission | SingerPermission | ListenerPermission]
    serializer_class = AdminUserUpdateSerializer
    queryset = User.objects.all()


class AdminUserDeleteView(DestroyAPIView):
    permission_classes = [AdminPermission | SingerPermission | ListenerPermission]
    queryset = User.objects.all()
