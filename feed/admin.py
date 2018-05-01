from django.contrib import admin
from feed.models import UserPost,UserComment

# Register your models here.
admin.site.register(UserPost)
admin.site.register(UserComment)