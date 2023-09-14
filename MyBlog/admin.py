from django.contrib import admin
from .models import Post
from .models import TopicPost
from .models import Photo_post




class MyBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'topic', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

class PhotopostAdmin(admin.ModelAdmin):
    list_display = ('images', 'post')

admin.site.register(Post, MyBlogAdmin)
admin.site.register(TopicPost)
admin.site.register(Photo_post, PhotopostAdmin)



