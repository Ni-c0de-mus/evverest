from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.choices import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	first_name = models.CharField(max_length=50,blank=False,default='User')
	join_date = models.DateTimeField(default=timezone.now)
	profile_pic = models.ImageField(upload_to='profile_pics',null=True,blank=True)
	location = models.CharField(max_length=150,blank=False)
	title = models.CharField(max_length=250)
	user_type = models.CharField(max_length=10,choices=USER_TYPE_CHOICES,default='1')
	website = models.URLField(max_length=100,blank=True)
	about = models.TextField(max_length=500,default='about')
	twitter = models.CharField(max_length=50,blank=True)
	dribbble = models.CharField(max_length=50,blank=True)
	github = models.CharField(max_length=50,blank=True)
	user_level = models.IntegerField(default=1)
	user_score = models.IntegerField(blank=False,default=10)
	
	def __str__(self):
		return self.user.username

# Creating instance in UserProfile model when main Users model gets new signup
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()


