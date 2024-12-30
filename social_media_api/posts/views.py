from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from posts.models import Post, Comment

# Create your views here.

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    