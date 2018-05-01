from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from feed.models import UserPost,UserComment
from users.models import UserProfile
from notify.models import UserNotification
from feed.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin

from django.views.generic import (TemplateView,ListView,
									DetailView,CreateView,
									UpdateView,DeleteView,
									RedirectView,)

User = get_user_model()

class UserNotifications(LoginRequiredMixin, ListView):
	login_url = 'account_login'
	model = UserNotification
	template_name = 'notify/usernotification_list.html'
	context_name = 'notifies'
	paginate_by = 5
	
	def get_queryset(self):
		return UserNotification.objects.filter(toUser=self.request.user)
	
	def get_context_data(self, **kwargs):
		context = super(UserNotifications, self).get_context_data(**kwargs)
		context["notifies"] = self.get_queryset().filter(toUser=self.request.user).order_by('-timestamp')
	
		return context

class NotifyMarkRead(RedirectView):
	def get_redirect_url(self,pk):
		obj = get_object_or_404(UserNotification,pk=pk)
		if obj.read == False:
			obj.read = True
			obj.save()
		else:
			obj.read = False
			obj.save()
		return obj.get_absolute_url()