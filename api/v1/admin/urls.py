from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.admin.user.urls')),
]
