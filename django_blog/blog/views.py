from django.shortcuts import render, redirect
from .forms import UserRegistration, ProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import UserProfile
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        form = UserRegistration()
    context = {"form": form}
    return render(request, "registration/register.html", context)

class Login(LoginView):
    template_name = 'registration/login.html'
    next_page = 'profile'

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

def logout_view(request):
    logout(request)
    redirect('login')
    return render(request, 'registration/logout.html')

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {"user_profile":user_profile}
    if request.method == 'POST':
        form = ProfileForm(request=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()
    return render(request, 'blog/profile.html', context)

