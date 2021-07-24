from django.shortcuts import render
from .models import Gallery, Category_images

# Create your views here.


def gallery(request):
    """ A view to show images, including sorting and search queries """

    images = Gallery.objects.all()
    category_images = None

    if request.GET:
        if 'category_images' in request.GET:
            category_images = request.GET['category_images'].split(',')
            images = images.filter(category_images__name__in=category_images)
            category_images = Category_images.objects.filter(name__in=category_images)
    context = {
        'images': images,
        'current_categories': category_images,
    }

    return render(request, 'gallery/images.html', context)
