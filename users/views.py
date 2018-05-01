from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from users.forms import UserForm,UserProfileForm
from users.models import UserProfile
from feed.models import UserPost
from feed.models import UserComment

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
									DetailView,CreateView,DeleteView)
from django.views.generic.edit import UpdateView

# Create your views here.
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def exploreView(request):
	posts = UserPost.objects.all()
	users = UserProfile.objects.all()
	new_users = users.order_by('-join_date')
	popular_users = users.order_by('-user_score')
	
	context = {
		'new_users':new_users,
		'popular_users':popular_users,
		'posts':posts,
	}
	
	return render(request,'users/explore.html',context)


# class UserListView(ListView):
# 	model = UserProfile
# 	ordering = ['-join_date']
# 	
# 	def get_context_data(self, **kwargs):
# 		context = super(UserListView, self).get_context_data(**kwargs)
# 		context['user_list'] = User.objects.all()
# 		return context

def singleUserProfile(request,pk):
	userprofile = UserProfile.objects.get(user=request.user)
	user = get_object_or_404(User,pk=pk)
	posts = UserPost.objects.filter(author=user)
	paginator = Paginator(posts, 10)
	
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	
	context = {
			'user':user,
			'userprofile':userprofile,
			'posts':posts,
		}
	
	return render(request,'users/userprofile_detail.html',context)

@login_required
def detailprofile(request):
	userprofile = UserProfile.objects.get(user=request.user)
	user = get_object_or_404(User,pk=request.user.pk)
	posts = UserPost.objects.filter(author=user)
	paginator = Paginator(posts, 10)
	
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	
	context = {
			'user':user,
			'userprofile':userprofile,
			'posts':posts,
		}
	
	return render(request,'users/userprofile_detail.html',context)

def editProfileView(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:user_profile'))
		else:
			return render(request, 'users/userprofile_edit_form.html')
	else:
		form = UserProfileForm(instance=request.user.userprofile)
		args = {'form':form}
		return render(request, 'users/userprofile_edit_form.html', args)


# class UserEditProfileView(LoginRequiredMixin,UpdateView):
# 	login_url = '/login/'
# 	model = UserProfile
# 	form_class = UserProfileForm
# 	template_name_suffix = '_edit_form'
# 	
# 	current_user = request.user
# 		
# 	print(userid)
# 	print(current_user)
# 	
# 	def get_success_url(self):
# 		userid = self.kwargs['pk']
# 		
# 		if userid == current_user:
# 			return reverse_lazy('users:user_profile',kwargs={'pk': userid})
# 		else:
# 			return reverse_lazy('users:explore')



















