from django.contrib import admin
from .models import User, Post, Friendship

admin.site.register(User)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'date', 'view_counter', 'friendship')
    list_display_links = ('id', 'author', 'text', 'date', 'view_counter', 'friendship')
    list_filter = ('friendship',)

admin.site.register(Post, PostAdmin)

admin.site.register(Friendship)