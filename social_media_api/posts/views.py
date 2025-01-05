from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets,  status, filters
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import django_filters.rest_framework
from posts.permissions import CustomUserPerm
from rest_framework import generics, views

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
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = CustomUser.objects.get(email=request.user)
        user.following.all()
       
        posts = Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
        # print(posts.title)
        serializer = PostSerializer(posts, many=True)
        return Response({"User feed": serializer.data})