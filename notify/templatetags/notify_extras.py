from notify.models import UserNotification
from django import template
from django.contrib.auth import get_user_model

register = template.Library()

@register.simple_tag(name='notseen')


def notseen(request):
	if UserNotification.objects.filter(toUser=request.user, read=False).exists():
		return True
	else:
		return False



# @register.simple_tag(name='notseen')
# def notseen(request):
# 	notifications = UserNotification.objects.filter(toUser=request.user, read=False)
# 	
# 	if notifications.exists():
# 		count = notifications.count()
# 		
# 		return count
# 	else:
# 		return False