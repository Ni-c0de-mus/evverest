from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
	url(r'^explore$',views.exploreView,name='explore'),
	url(r'^(?P<pk>\d+)/$',views.singleUserProfile,name='single_user_profile'),
	url(r'^profile$',views.detailprofile,name='user_profile'),
	url(r'^edit$',views.editProfileView,name='user_profile_edit'),
#	url(
#		regex=r'^profile/edit$',
#		view=views.UserEditProfileView.as_view(),
#		name='user_profile_edit'
#    ),
]