from django.urls import path, include

urlpatterns = [
    path('admin/', include('api.v1.admin.urls')),
]
