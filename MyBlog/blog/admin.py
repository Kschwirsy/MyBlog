from django.contrib import admin
from blog.models import Post
from blog.models import PostAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from blog.models import Comment
from blog.models import CommentAdmin

admin.site.register(Post, PostAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
