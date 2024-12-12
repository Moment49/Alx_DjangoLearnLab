from django.shortcuts import render, redirect
from .forms import UserRegistration, UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import UserProfile, User
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
    return render(request, "blog/register.html", context)

class Login(LoginView):
    template_name = 'blog/login.html'
    next_page = 'profile'

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

def logout_view(request):
    logout(request)
    redirect('login')
    return render(request, 'registration/logout.html')

def profile(request):
    user_profile = UserProfile.objects.get(user__username=request.user)
    context = {"user_profile":user_profile}
    return render(request, 'blog/profile.html', context)

def edit_profile(request, user):
    user = User.objects.get(username=user)
    user_pro = UserProfile.objects.get(user__username=user)
    if request.method == 'POST':
        form_profile = ProfileForm(request.POST, request.FILES)
        print(form_profile)
        form_user = UserForm(request.POST)
        if form_profile.is_valid() and form_user.is_valid():
            email= form_user.cleaned_data['email']
            bio = form_profile.cleaned_data['bio']
            print(bio)
            date_of_birth = form_profile.cleaned_data['date_of_birth']
            age = form_profile.cleaned_data['age']
            profile_img = form_profile.cleaned_data['profile_img']
            user.email = email
            user_pro.profile_img = profile_img
            user_pro.bio = bio
            user_pro.date_of_birth = date_of_birth
            user_pro.age = age
            user_pro.save()
            user.save()
            return redirect('profile')
    else:
        form_profile = ProfileForm()
        form_user= UserForm()
    return render(request, 'blog/edit_profile.html', {"form_profile":form_profile, "form_user":form_user})

