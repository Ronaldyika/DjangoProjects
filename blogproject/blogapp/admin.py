from django.contrib import admin
from .models import BlogPost,BlogShare,Comment,UserProfile
admin.site.register(BlogPost)
admin.site.register(BlogShare)
admin.site.register(Comment)
admin.site.register(UserProfile)