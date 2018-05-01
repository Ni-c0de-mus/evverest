from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile
from users.choices import *

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta():
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
	profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control mb-3'}), required=False)
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
	user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
	website = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}), required=False)
	about = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-3'}))
	twitter = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}), required=False)
	dribbble = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}), required=False)
	github = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}), required=False)
	
	class Meta:
		model = UserProfile
		fields = (
			'first_name',
			'profile_pic',
			'location',
			'title',
			'user_type',
			'website',
			'about',
			'twitter',
			'dribbble',
			'github'
		)