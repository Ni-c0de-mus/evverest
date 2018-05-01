from django.conf.urls import url
from notify import views

app_name = 'notify'

urlpatterns = [
	url(r'^$',views.UserNotifications.as_view(),name='user_notifications'),
	url(r'^(?P<pk>\d+)/read/$',views.NotifyMarkRead.as_view(),name='user_notify_toggle'),
]