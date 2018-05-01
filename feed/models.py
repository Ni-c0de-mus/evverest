from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserPost(models.Model):
	author = models.ForeignKey(User,related_name='userpost',null=True)
	post_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=150,blank=False)
	post_body = RichTextField(default='Text')
	image = models.ImageField(upload_to='post_pics',blank=True)
	likes = models.ManyToManyField(User,blank=True,related_name='post_likes')
	
	class Meta:
		ordering = ['-post_date']
	
	def publish(self):
		self.save()
	
	def get_absolute_url(self):
		return reverse('index')
		
	def likes_as_flat_user_id_list(self):
		return self.likes.values_list('id', flat=True)
	
	def __str__(self):
		return self.title

class UserComment(models.Model):
	post = models.ForeignKey('feed.UserPost',related_name='comments')
	author = models.ForeignKey(User,related_name='usercomment')
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_body = models.TextField(max_length=500)
	
	class Meta:
		ordering = ['-comment_date']
	
	def publish(self):
		self.save()
	
	def get_absolute_url(self):
		return reverse("userpost_list")
	
	def __str__(self):
		return self.author