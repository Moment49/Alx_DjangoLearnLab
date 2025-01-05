from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets,  status, filters
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment, Like
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import django_filters.rest_framework
from posts.permissions import CustomUserPerm
from rest_framework import generics, views
from rest_framework import permissions

CustomUser = get_user_model()



# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, CustomUserPerm]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['content', 'title']
    search_fields=["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        return self.request.user.posts.all()
    

class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['post', 'content']
    search_fields=["post", "content"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.request.user.comments.all()

class UserFeedView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = CustomUser.objects.get(email=request.user)
        following_users = user.following.all()
       
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response({"User feed": serializer.data})

class LikePost(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):
        user = CustomUser.objects.get(email=request.user)
        post = Post.objects.get(pk=pk)
        Like.objects.get_or_create(user=user, post=post)

        return Response({"message": "post liked"})
    
class UnLikePost(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):
        user = CustomUser.objects.get(email=request.user)
        post = Post.objects.get(pk=pk)
        liked_post = Like.objects.get(post=post)
        liked_post.delete()

        return Response({"message": "post unliked"})
