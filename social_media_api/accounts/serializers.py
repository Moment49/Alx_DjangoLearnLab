from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "username"]

class RegisterationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if len(password) and len(confirm_password) >= 7:
            if password != confirm_password:
                raise ValidationError("Password does not match")
        else:
            raise ValidationError("Password must be above 7 characters")
        return attrs
    
    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        # pop/remove the confirm_password field from the validated_data and pass it to the User model
        confirm_password = validated_data.pop('confirm_password')
        # Create the user
        user = User.objects.create_user(email=email, password=password, **validated_data)

        return user
       
      
    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
    
 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
