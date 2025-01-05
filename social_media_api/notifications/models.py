from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey


CustomUser = get_user_model()

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    # actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    # verb = models.CharField()
    # object_id = models.PositiveIntegerField()
    # target = GenericForeignKey("object_id")
    # timestamp = models.DateTimeField(auto_now=True)

  