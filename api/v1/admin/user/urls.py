from django.urls import path
from api.v1.admin.user import views

urlpatterns = [
    # USER
    path('create/', views.AdminUserCreateView.as_view()),
    path('list/', views.AdminUserListView.as_view()),
    path('detail/<int:pk>/', views.AdminUserDetailView.as_view()),
    path('update/<int:pk>/', views.AdminUserUpdateView.as_view()),
    path('delete/<int:pk>/', views.AdminUserDeleteView.as_view())
]
