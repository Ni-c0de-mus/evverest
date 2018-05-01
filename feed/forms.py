from django import forms
from feed.models import UserPost,UserComment
from users.models import UserProfile

from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mb-3'}), required=False)
	post_body = forms.CharField(widget=CKEditorWidget())
	
	class Meta:
		model = UserPost
		fields = ('title','image','post_body')

class CommentForm(forms.ModelForm):
	comment_body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-3'}))
	
	class Meta:
		model = UserComment
		fields = ('comment_body',)