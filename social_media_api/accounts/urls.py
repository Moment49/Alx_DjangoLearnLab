from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token

# router = DefaultRouter()

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.login_view, name="login"),
    path('token/', obtain_auth_token)  
]

