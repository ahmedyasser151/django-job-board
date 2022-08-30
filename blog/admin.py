from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'created_on',
        'category',
        'status',
    ]

    list_filter = ("status", 'category',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)