from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


CustomUser = get_user_model()

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="recipent_notifications")
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="actor_notifications")
    verb = models.CharField(max_length=100)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey( "content_type", "object_id")
    timestamp = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)

  