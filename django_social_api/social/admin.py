from django.contrib import admin
from .models import SocialUser, Post, Like

admin.site.register(Like)
admin.site.register(Post)
admin.site.register(SocialUser)