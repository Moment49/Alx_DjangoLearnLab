from rest_framework.generics import CreateAPIView
from accounts.serializers import RegisterationSerializer, LoginSerializer, ProfileSerializer
from accounts.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterationSerializer
    model = User

    # Revisit this to understand concept very well
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response({'username': serializer.data}, status=201)


@api_view(['POST', 'GET'])
def login_view(request):
    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"user_data": serializer.data, 'token':token.key}, 200)
            else:
                print("Not authenticated") 
                raise ValueError("User not authenticated")  
    else:
        return Response({"user":"THE LOGIN"})

class ProfileView(LoginRequiredMixin, APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = User.objects.get(email=request.user.email)
        user_profile = UserProfile.objects.get(user=user)

        serializer = ProfileSerializer(user_profile)       
        return Response({"profile_data": serializer.data})
    
    def patch(self, request):
        # Method to partial update user profile records
        user = User.objects.get(email=request.user)
        user_profile = UserProfile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, data=request.data, partial=True)
      
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': f'Resource user_profile updated successfully', "user_profile":serializer.data},status=status.HTTP_200_OK)
        else:
            print("Bad request")
            return Response({'message': "Bad Request"},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        # Method to partial update user profile records
        user = User.objects.get(email=request.user)
        user_profile = UserProfile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, data=request.data)
      
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': f'Resource user_profile updated successfully', "user_profile":serializer.data}, status=status.HTTP_200_OK)
        else:
            print("Bad request")
            return Response({'message': "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


