from django.contrib import admin

# Register your models here.
from .models import Post
# from .models import Dash

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_display_links = ['updated']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
