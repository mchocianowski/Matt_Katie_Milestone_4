from django.contrib import admin
from .models import Gallery, Category_images

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category_images',
        'rating',
        'image',
    )

    ordering = ('name',)


class Category_imagesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category_images, Category_imagesAdmin)
