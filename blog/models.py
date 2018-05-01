from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class BlogPost(models.Model):
	author = models.ForeignKey(User, related_name='blogpost',null=True)
	post_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=150,blank=False)
	post_body = models.TextField(max_length=1000,blank=False)
	image = models.ImageField(upload_to='blog_pics',blank=True)
	
	class Meta:
		ordering = ['-post_date']
	
	def publish(self):
		self.save()
	
	def get_absolute_url(self):
		return reverse('blog:blog')
	
	def __str__(self):
		return self.title

class BlogComment(models.Model):
	post = models.ForeignKey('blog.BlogPost',related_name='comments')
	author = models.ForeignKey(User,related_name='blogcomment')
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_body = models.TextField(max_length=500)
	
	class Meta:
		ordering = ['-comment_date']
	
	def publish(self):
		self.save()
	
	def get_absolute_url(self):
		return reverse('blogpost_list')
	
	def __str__(self):
		return self.author