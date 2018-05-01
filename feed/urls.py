from django.conf.urls import url
from feed import views

app_name = 'feed'

urlpatterns = [
	url(r'^new/$',views.createPost,name='new_post'),
	url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
	url(r'^post/(?P<pk>\d+)/like/$',views.LikePostToggle.as_view(),name='post_like'),
	url(r'^post/(?P<pk>\d+)/edit/$',views.UpdatePostView.as_view(),name='edit_post'),
	url(r'^post/(?P<pk>\d+)/delete/$',views.DeletePost,name='delete_post'),
	url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment'),
	url(r'^post/(?P<pk>\d+)/delete-comment/$',views.comment_remove,name='remove_comment'),
	
]