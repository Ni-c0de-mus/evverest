from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

User = get_user_model()

# Create your models here.
class UserNotification(models.Model):
	fromUser = models.ForeignKey(User,related_name='user',null=True)
	post = models.ForeignKey('feed.UserPost',related_name='post')
	toUser = models.CharField(max_length=6,default='user')
	timestamp = models.DateTimeField(auto_now_add=True)
	notify_type = models.CharField(max_length=6)
	read = models.BooleanField(default=False)
	
	def get_absolute_url(self):
		return reverse('notify:user_notifications')
	
	def __str__(self):
		return str(self.fromUser)