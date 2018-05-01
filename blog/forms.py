from django import forms
from blog.models import BlogPost,BlogComment
from users.models import UserProfile

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ('title','post_body','image',)
		
		widget = {
			'title':forms.TextInput(attrs={'class':'post-title'}),
			'post_body':forms.Textarea(attrs={'class':'post-body'}),
		}

class BlogCommentForm(forms.ModelForm):
	class Meta:
		model = BlogComment
		fields = ('comment_body',)
		
		widgets = {
			'comment_body':forms.Textarea(attrs={'class':'comment-body'}),
		}