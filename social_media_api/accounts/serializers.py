from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from accounts.models import UserProfile


CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'following', 'followers']


class RegisterationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'bio', 'profile_picture', 'password', 'confirm_password', 'token']
        

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        # This will convert the token to a serializable string
        token = str(token)
        return token

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
        # pop/remove the confirm_password field from the validated_data and pass the rest of the data to the User model
        confirm_password = validated_data.pop('confirm_password')

        # Create the user
        user = get_user_model().objects.create_user(email=email, password=password, **validated_data)

        # Create the Token
        Token.objects.create(user=user)

        return user


 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    bio = serializers.CharField(write_only=True)
    profile_pic = serializers.ImageField(write_only=True)
   
    class Meta:
        model = UserProfile
        fields = ['user_id', 'user_profile', 'first_name', 'last_name', 'bio', 'profile_pic']
    
    def get_user_profile(self, obj):
        user_profile_data = {"first_name":obj.user.first_name, 
                             "last_name": obj.user.last_name,
                             "email":obj.user.email,
                             "bio": obj.user.bio,
                             "img":obj.user.profile_picture.url
                            }
    
        return user_profile_data
    
    def update(self, instance, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        bio = validated_data.get('bio')
        profile_pic = validated_data.get('profile_pic')

        # Note the instance is the obj instance of the user profile which defaults to the email
        # update the user details from the user_profile
        instance.user.first_name = first_name
        instance.user.last_name = last_name
        instance.user.bio = bio
        instance.user.profile_picture = profile_pic
        instance.save()

        user = CustomUser.objects.get(email=instance.user.email)
        user.first_name = first_name
        user.last_name = last_name
        user.bio = bio
        user.profile_picture = profile_pic

        # Save to db
        user.save()

        return instance