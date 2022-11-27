from django.urls import path
from api.v1.admin.music_library import views

urlpatterns = [
    # LICENSE
    path('license/create/', views.AdminLicenseCreateView.as_view()),
    path('license/list/', views.AdminLicenseListView.as_view()),
    path('license/detail/<int:pk>/', views.AdminLicenseDetailView.as_view()),
    path('license/update/<int:pk>/', views.AdminLicenseUpdateView.as_view()),
    path('license/delete/<int:pk>/', views.AdminLicenseDeleteView.as_view()),

]
