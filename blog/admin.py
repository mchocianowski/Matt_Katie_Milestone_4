from django.contrib import admin
from .models import Post, Category_blog

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class Category_blogAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Category_blog, Category_blogAdmin)
