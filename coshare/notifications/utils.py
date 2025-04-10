# notifications/utils.py

from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(user, title, message, icon_url=None):
    notification = Notification.objects.create(
        user=user,
        title=title,
        message=message,
        icon_url=icon_url
    )

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}",
        {
            "type": "send_notification",
            "content": {
                "title": notification.title,
                "message": notification.message,
                "icon": notification.icon_url
            }
        }
    )
