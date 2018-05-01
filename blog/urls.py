from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
	url(r'^$',views.BlogView.as_view(),name='blog'),
	url(r'^blog/new/$',views.CreateBlogPostView.as_view(),name='new_blog_post'),
	url(r'^blog/(?P<pk>\d+)$',views.BlogPostDetailView.as_view(),name='blogpost_detail'),
	url(r'^blog/(?P<pk>\d+)/edit/$',views.UpdateBlogPostView.as_view(),name='edit_blogpost'),
	url(r'^blog/(?P<pk>\d+)/delete/$',views.DeleteBlogPost,name='delete_blogpost'),
	url(r'^blog/(?P<pk>\d+)/comment/$',views.add_comment_to_blogpost,name='add_blog_comment'),
	url(r'^blog/(?P<pk>\d+)/delete-comment/$',views.blog_comment_remove,name='remove_blog_comment'),
]