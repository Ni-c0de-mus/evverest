from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import BlogPost,BlogComment
from blog.forms import BlogPostForm,BlogCommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin

from django.views.generic import (TemplateView,ListView,
									DetailView,CreateView,
									UpdateView,DeleteView)

User = get_user_model()

# Create your views here.
class BlogView(ListView):
	model = BlogPost
	template_name = 'blog/userpost_list.html'
#	context_object_name = 'posts'
	paginate_by = 25
	queryset = BlogPost.objects.all()

class CreateBlogPostView(LoginRequiredMixin,CreateView):
	login_url = 'users:user_login'
	redirect_field_name = '/blogpost_list.html'
	model = BlogPost
	form_class = BlogPostForm
	
	def form_valid(self,form):
		form.instance.author = self.request.user
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(CreateBlogPostView, self).form_valid(form)

class BlogPostDetailView(DetailView):
	model = BlogPost
	blog_comments = BlogComment.objects.all()
	context = {
		'blogpost':model,
		'blogcomments':blog_comments
	}

class UpdateBlogPostView(LoginRequiredMixin,UpdateView):
	login_url = '/login/'
	model = BlogPost
	fields = [
		'title',
		'post_body',
		'image',
		]
	template_name_suffix = '_edit_form'
	
	def get_success_url(self):
		blogpostid = self.kwargs['pk']
		return reverse_lazy('blog:blog')

@login_required
def DeleteBlogPost(request,pk):
	blogpost = get_object_or_404(BlogPost,pk=pk)
	blogpost.delete()
	return redirect('blog:blog')


##Blog Comment Views
@login_required
def add_comment_to_blogpost(request,pk):
	post = get_object_or_404(BlogPost,pk=pk)
	if request.method == 'POST':
		form = BlogCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('blog:blogpost_detail',pk=post.pk)
	else:
		form = BlogCommentForm()
	return render(request,'blog/comment_form.html',{'form':form})

@login_required
def blog_comment_remove(request,pk):
	comment = get_object_or_404(BlogComment,pk=pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('blog:blogpost_detail',pk=post_pk)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	