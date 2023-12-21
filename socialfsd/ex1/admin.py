from django.contrib import admin
from .models import User, Post

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'bio', 'username', 'password', 'email')
    list_display_links = ('id', 'bio', 'username', 'password', 'email')
    list_per_page = 20
    search_fields = ('user__username', 'bio', 'username', 'password', 'email')
    
admin.site.register(User, UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'date', 'view_counter')
    list_display_links = ('id', 'author', 'text', 'date', 'view_counter')
    list_per_page = 20
    search_fields = ('author', 'text')
    
admin.site.register(Post, PostAdmin)