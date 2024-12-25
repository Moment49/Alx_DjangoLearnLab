from rest_framework.generics import CreateAPIView
from accounts.serializers import RegisterationSerializer, LoginSerializer, TokenSerializer
from accounts.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterationSerializer
    model = User

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        print(user)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key, 'username': serializer.instance.username}, status=201)

    def perform_create(self, serializer):
        serializer.save()

@api_view(['POST', 'GET'])
def login_view(request):
    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                print(serializer.instance)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"user_data": serializer.data, 'token':token.key}, 201)
            else:
                print("Not authenticated") 
                raise ValueError("User not authenticated")  
    else:
        return Response({"user":"THE LOGIN"})



