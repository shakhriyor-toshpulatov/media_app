from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from api.v1.admin.music_library.serializers import *
from api.v1.permissions import AdminPermission, SingerPermission, ListenerPermission
from music_library.models import *


# --------------------------License-----------------------------
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


# ------------------------Album-------------------------------
class AdminAlbumCreateView(CreateAPIView):
    permission_classes = [SingerPermission]
    serializer_class = AdminAlbumCreateSerializer


class AdminAlbumListView(ListAPIView):
    permission_classes = [SingerPermission | AdminPermission | ListenerPermission]
    serializer_class = AdminAlbumListSerializer
    queryset = Album.objects.all()


class AdminAlbumDetailView(RetrieveAPIView):
    permission_classes = [SingerPermission | AdminPermission | ListenerPermission]
    serializer_class = AdminAlbumDetailSerializer
    queryset = Album.objects.all()


class AdminAlbumUpdateView(UpdateAPIView):
    permission_classes = [SingerPermission]
    serializer_class = AdminAlbumUpdateSerializer
    queryset = Album.objects.all()


class AdminAlbumDeleteView(DestroyAPIView):
    permission_classes = [SingerPermission | AdminPermission]
    queryset = Album.objects.all()


# ------------------------Track---------------------------
class AdminTrackCreateView(CreateAPIView):
    permission_classes = [SingerPermission]
    serializer_class = AdminTrackCreateSerializer


class AdminTrackListView(ListAPIView):
    permission_classes = [SingerPermission | AdminPermission | ListenerPermission]
    serializer_class = AdminTrackListSerializer
    queryset = Track.objects.all()


class AdminTrackDetailView(RetrieveAPIView):
    permission_classes = [SingerPermission | AdminPermission | ListenerPermission]
    serializer_class = AdminTrackDetailSerializer
    queryset = Track.objects.all()


class AdminTrackUpdateView(UpdateAPIView):
    permission_classes = [SingerPermission]
    serializer_class = AdminTrackUpdateSerializer
    queryset = Track.objects.all()


class AdminTrackDeleteView(DestroyAPIView):
    permission_classes = [SingerPermission | AdminPermission]
    queryset = Track.objects.all()
