from django.shortcuts import render, redirect
from .forms import UserRegistration, UserForm, ProfileForm, PostForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, User, Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class HomeBlogPostList(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "all_posts"

def dashboard(request):
    all_posts = Post.objects.all()
    context = {"all_posts": all_posts}
    return render (request, "blog/dashboard.html", context)

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
    next_page = 'dashboard'

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

def logout_view(request):
    logout(request)
    redirect('login')
    return render(request, 'registration/logout.html')

@login_required
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

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "singlepost"
 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            print("Valid User")
            return self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            print("Valid User")
            return self.request.user

    