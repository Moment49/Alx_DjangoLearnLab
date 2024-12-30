from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.login_view, name="login"),
    path('profile/', views.ProfileView.as_view(), name="profile")
]

