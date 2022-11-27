from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.admin.user.urls')),
    path('music-library/', include('api.v1.admin.music_library.urls')),
]
