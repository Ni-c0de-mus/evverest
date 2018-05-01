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

from django.db.models import F

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin

from django.views.generic import (TemplateView,ListView,
									DetailView,CreateView,
									UpdateView,DeleteView,RedirectView)

User = get_user_model()

# Create your views here.

##Posts Views
@login_required
def HomeView(request):
	login_url = 'account_login'
	posts = UserPost.objects.all()
	paginator = Paginator(posts, 15)
	
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
		'posts' : posts
	}
	
	return render(request, 'feed/userpost_list.html', context)


@login_required
def createPost(request):
	user = UserProfile.objects.get(user=request.user)
	current_score = user.user_score
	
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			user.user_score = current_score - 1
			user.save()
			post.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request,'feed/userpost_form.html',{'form':form})
	


class CreatePostView(LoginRequiredMixin,CreateView):
	login_url = 'account_login'
	redirect_field_name = '/userpost_list.html'
	model = UserPost
	form_class = PostForm
# 	user_score = User.userprofile.user_score
	
	def form_valid(self,form):
		form.instance.author = self.request.user
# 		User.userprofile.user_score = user_score - 1
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(CreatePostView, self).form_valid(form)

class PostDetailView(LoginRequiredMixin,DetailView):
	model = UserPost
	post_comments = UserComment.objects.all().order_by('comment_date')
	context = {
			'post':model,
			'comments':post_comments,
			}


class UpdatePostView(LoginRequiredMixin,UpdateView):
	login_url = 'account_login'
	model = UserPost
	form_class = PostForm
	template_name_suffix = '_edit_form'
	
	def get_success_url(self):
#		postid = self.kwargs['pk']
		return reverse_lazy('index')

class LikePostToggle(RedirectView):
	def get_redirect_url(self,pk):
		post = get_object_or_404(UserPost,pk=pk)
		author = UserProfile.objects.get(user=post.author)
		user = self.request.user
		if user.is_authenticated():
			if user in post.likes.all():
				post.likes.remove(user)
				author.user_score = F('user_score') - 1
				author.save()
			else:
				post.likes.add(user)
				author.user_score = F('user_score') + 1
				author.save()
				notification = UserNotification.objects.create(
					fromUser = self.request.user,
					toUser = post.author,
					post = post,
					notify_type = "like",
				)
		return post.get_absolute_url()


@login_required
def DeletePost(request,pk):
	post = get_object_or_404(UserPost,pk=pk)
	author = UserProfile.objects.get(user=post.author)
	author.user_score = F('user_score') - 5
	author.save()
	post.delete()
	return redirect('index')

##Comments Views
@login_required
def add_comment_to_post(request,pk):
	post = get_object_or_404(UserPost,pk=pk)
	author = UserProfile.objects.get(user=post.author)
	current_user = UserProfile.objects.get(user=request.user)
	
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			author.user_score = F('user_score') + 3
			current_user.user_score = F('user_score') + 2
			current_user.save()
			author.save()
			comment.save()
			notification = UserNotification.objects.create(
				fromUser = request.user,
				toUser = post.author,
				post = post,
				notify_type = "comment",
			)
			return redirect('feed:post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request,'feed/comment_form.html',{'form':form})

@login_required
def comment_remove(request,pk):
	comment = get_object_or_404(UserComment,pk=pk)
	post_pk = comment.post.pk
	author = UserProfile.objects.get(user=comment.author)
	author.user_score = F('user_score') - 2
	
	author.save()
	comment.delete()
	return redirect('feed:post_detail',pk=post_pk)





























