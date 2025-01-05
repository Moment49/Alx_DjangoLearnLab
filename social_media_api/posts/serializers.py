from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth import get_user_model
import re
from rest_framework.validators import ValidationError



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', "email", "username"]


class PostSerializer(serializers.ModelSerializer):
    author =  UsersSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
    

    def validate(self, attrs):
        regex = re.compile('[0-9@_!#$%^&*()<>?/\|}{~:]')
        title = attrs.get('title')
        if len(title) > 100 or regex.search(title) != None:
            raise ValidationError("Title must not contain special characters or numbers and should be less than 100 characters")
        return attrs
       

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = UsersSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['post', 'user', 'content']
    
    def create(self, validate_data):
        post = validate_data.pop('post')
        post = Post.objects.get(title=post['title'])

        comment = Comment.objects.create(post=post, **validate_data)
        comment.save()
        return comment
    
    def update(self, instance, validate_data):
        comment = validate_data.pop('content')
        instance.content = comment
        instance.save()

        return instance