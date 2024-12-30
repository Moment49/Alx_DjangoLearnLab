from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = UserSerializer()
    class Meta:
        models = Comment
        fields = ['post', 'user', 'content']