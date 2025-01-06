from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer

# CustomUser = get_user_model()

# Create your views here.

class NotificationView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications= Notification.objects.filter(recipient=request.user).order_by("-timestamp")
        for n in notifications:   
            # Serialize notification data to json format  
            rec_ser = UserSerializer(n.recipient)
            act_ser = UserSerializer(n.actor)
            notification_data = {"recipient": rec_ser.data,
                "sender":act_ser.data,
                "message":n.verb,
                "timestamp":n.timestamp,
                "read":n.read
                }
        return Response({"Notification": notification_data}, 200)