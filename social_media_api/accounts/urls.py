from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.login_view, name="login"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', views.UnFollowUserView.as_view(), name='unfollow'),
  
]

