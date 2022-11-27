from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from api.v1.admin.music_library.serializers import *
from api.v1.permissions import AdminPermission, SingerPermission, ListenerPermission
from music_library.models import *


class AdminLicenseCreateView(CreateAPIView):
    permission_classes = [SingerPermission]
    serializer_class = AdminLicenseCreateSerializer


class AdminLicenseListView(ListAPIView):
    permission_classes = [AdminPermission | SingerPermission | ListenerPermission]
    serializer_class = AdminLicenseListSerializer
    queryset = License.objects.all()


class AdminLicenseDetailView(RetrieveAPIView):
    permission_classes = [AdminPermission | SingerPermission | ListenerPermission]
    serializer_class = AdminLicenseDetailSerializer
    queryset = License.objects.all()


class AdminLicenseUpdateView(UpdateAPIView):
    permission_classes = [AdminPermission | SingerPermission]
    serializer_class = AdminLicenseUpdateSerializer
    queryset = License.objects.all()


class AdminLicenseDeleteView(DestroyAPIView):
    permission_classes = [AdminPermission | SingerPermission]
    queryset = License.objects.all()
