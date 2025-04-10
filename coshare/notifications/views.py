from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Notification

@login_required
def mark_as_read(request, pk):
    try:
        notif = Notification.objects.get(pk=pk, user=request.user)
        notif.is_read = True
        notif.save()
        return JsonResponse({'status': 'ok'})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

@login_required
def delete_notification(request, pk):
    try:
        notif = Notification.objects.get(pk=pk, user=request.user)
        notif.delete()
        return JsonResponse({'status': 'deleted'})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)
    

@login_required
def mark_all_read(request):
    if request.method == 'POST':
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'invalid method'}, status=405)

