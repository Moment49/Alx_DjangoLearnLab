from rest_framework.generics import CreateAPIView, GenericAPIView
from accounts.serializers import RegisterationSerializer, LoginSerializer, ProfileSerializer, UserSerializer
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
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import generics, viewsets
from rest_framework import permissions, validators


CustomUser = get_user_model()
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterationSerializer


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
        user = CustomUser.objects.get(email=request.user.email)
        user_profile = UserProfile.objects.get(user=user)

        serializer = ProfileSerializer(user_profile)       
        return Response({"profile_data": serializer.data})
    
    def patch(self, request):
        # Method to partial update user profile records
        user = CustomUser.objects.get(email=request.user)
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
        user = CustomUser.objects.get(email=request.user)
        user_profile = UserProfile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, data=request.data)
      
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': f'Resource user_profile updated successfully', "user_profile":serializer.data}, status=status.HTTP_200_OK)
        else:
            print("Bad request")
            return Response({'message': "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id=None):
        if request.data['action'] == 'follow_user':
            user_to_be_followed = CustomUser.objects.get(pk=user_id)
            if self.request.user == user_to_be_followed:
                raise Response({"message":"You can not follow yourself"}, status=status.HTTP_403_FORBIDDEN)
            else:
                user = CustomUser.objects.get(email=request.user)
                users_follow_list = user.following.all()
               
                if user_to_be_followed in users_follow_list:
                    raise validators.ValidationError("You are already following user")
                
                user.following.add(user_to_be_followed)
                follower_count = user.following.all().count()
                serializer = UserSerializer(user)
        return Response ({"message":f"You are following {user_to_be_followed} now", "user_data":serializer.data, "following_count":{follower_count}}, 201)

class UnFollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id=None):
        if request.data['action'] == 'unfollow_user':
            user_to_be_unfollowed = CustomUser.objects.get(id=user_id)
            user = CustomUser.objects.get(email=request.user)
            users_follow_list = user.following.all()
            print(users_follow_list)
            if user_to_be_unfollowed in users_follow_list:
                user.following.remove(user_to_be_unfollowed)
                follower_count = users_follow_list.count()
            else:
                raise validators.ValidationError("You have alreaady Unfollowed user")
            
        return Response({"message": f"You have unfollowed {user_to_be_unfollowed} now", "follow_count":follower_count})
                


   

    
  