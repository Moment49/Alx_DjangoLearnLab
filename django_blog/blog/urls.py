from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeBlogPostList.as_view(), name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/<str:user>', views.edit_profile, name="edit_profile"),
    path('posts/', views.BlogPostListView.as_view(), name="all_posts"),
    path('posts/<int:pk>', views.BlogPostDetailView.as_view(), name="detail_post"),
    path('post/new', views.CreateView.as_view(), name="create_post"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('post/<int:pk>/update/', views.UpdateView.as_view(), name="update_post"),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name="delete_post"),
]