from django.shortcuts import render, redirect
from .forms import UserRegistration, UserForm, ProfileForm, PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, User, Post, Comment
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
 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Modify the form to save the tags and associate it
        print(form)
        tags = form.cleaned_data['tags']
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        tag_ = ''
        for tag in tags:
            tag_ += tag
        post = Post.objects.create(title=title, content=content, author=form.instance.author)
        post.tags.add(tag_)
        post.save()
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


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context_data =  super().get_context_data(**kwargs)
        post_id = self.kwargs['pk']
        comment = Comment.objects.filter(post=post_id)
        context_data['comment_data'] = comment
        context_data['comment_form'] = CommentForm
        return context_data

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_edit.html'

    def get_success_url(self):
        return reverse_lazy('detail_post', kwargs={"pk": self.object.post.id})
    
    def test_func(self):
        comment = self.get_object()
        if comment.post.author == self.request.user:
            return self.request.user

    
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    

    def get_success_url(self):
        return reverse_lazy('detail_post', kwargs={"pk":self.object.post.id})
    
    def test_func(self):
        comment = self.get_object()
        if comment.post.author == self.request.user:
            return self.request.user

def CommentCreateView(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment.objects.create(content=content, post=post, author=request.user)
            comment.save()
            return redirect('detail_post', pk=post.id)
    
    return render(request, 'blog/comment_create.html')