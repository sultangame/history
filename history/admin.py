from django.contrib import admin
from .models import Post, Category, Author
from django.contrib.auth.admin import GroupAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', 'category']
    list_filter = ['status', 'crated', 'publish', 'author', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author', 'category']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish', 'category']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    search_fields = ['category']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    raw_id_fields = ['user']
