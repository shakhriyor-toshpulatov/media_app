from django.urls import path
from . import views

urlpatterns = [
    path('refresh/', views.RefreshTokenView.as_view()),
    path('access/', views.ObtainTokenPairView.as_view()),
    path('logout/', views.APILogoutView.as_view()),
]
