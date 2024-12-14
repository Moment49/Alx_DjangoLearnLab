from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeBlogPostList.as_view(), name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/<str:user>', views.edit_profile, name="edit_profile"),
    path('posts/', views.PostListView.as_view(), name="all_posts"),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name="detail_post"),
    path('post/new/', views.PostCreateView.as_view(), name="create_post"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="update_post"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete_post"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # path('posts/<int:post_id>/comments/', views.CommentList.as_view(), name="comments"),
    path('posts/<int:post_id>/comments/', views.comment_list, name="comments"),
    
]