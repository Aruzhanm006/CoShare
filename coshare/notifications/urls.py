from django.urls import path
from .views import mark_as_read, delete_notification, mark_all_read

urlpatterns = [
    path('mark-read/<int:pk>/', mark_as_read, name='mark_as_read'),
    path('delete/<int:pk>/', delete_notification, name='delete_notification'),
    path('mark-all-read/', mark_all_read, name='mark_all_read'),
]
