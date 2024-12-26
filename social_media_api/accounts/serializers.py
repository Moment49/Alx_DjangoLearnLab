from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError


User = get_user_model()

class RegisterationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'bio', 'profile_picture', 'password', 'confirm_password', 'token']
        

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        print(type(token))
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
        # pop/remove the confirm_password field from the validated_data and pass it to the User model
        confirm_password = validated_data.pop('confirm_password')
        # Create the user
        user = get_user_model().objects.create_user(email=email, password=password, **validated_data)

        # Create the Token
        Token.objects.create(user=user)

        return user


 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        attrs.get('email')
