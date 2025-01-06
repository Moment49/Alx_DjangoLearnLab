from django.contrib import admin
from notifications.models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["recipient", "actor", "target", "object_id", "verb", "content_type", "read"]

admin.site.register(Notification, NotificationAdmin)