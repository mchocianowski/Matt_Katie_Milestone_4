from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Gallery, Category_images
from .forms import GalleryForm
# Create your views here.


def gallery(request):
    """ A view to show images, including sorting and search queries """

    images = Gallery.objects.all()
    category_images = None

    if request.GET:
        if 'category_images' in request.GET:
            category_images = request.GET['category_images'].split(',')
            images = images.filter(category_images__name__in=category_images)
            category_images = (
                Category_images.objects.filter(name__in=category_images)
            )
    context = {
        'images': images,
        'current_categories': category_images,
    }

    return render(request, 'gallery/images.html', context)


@login_required
def add_image(request):
    """ Add an image to the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can access these settings.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)

        if form.is_valid():
            gallery = form.save()
            messages.success(request, 'Successfully added image!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, "Failed to add image." +
                           "Please ensure the form is valid.")
    else:
        form = GalleryForm()

    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_image(request, gallery_id):
    """ Edit an image in the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can access these settings.')
        return redirect(reverse('home'))

    gallery = get_object_or_404(Gallery, pk=gallery_id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated image, title and details!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, "Failed to update image." +
                           "Please ensure the form is valid.")
    else:
        form = GalleryForm(instance=gallery)
        messages.info(request, f'You are editing {gallery.name}')

    template = 'gallery/edit_image.html'
    context = {
        'form': form,
        'gallery': gallery,
    }

    return render(request, template, context)


@login_required
def delete_image(request, gallery_id):
    """ Delete an image from the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can access these settings.')
        return redirect(reverse('home'))

    gallery = get_object_or_404(Gallery, pk=gallery_id)
    gallery.delete()
    messages.success(request, 'Image deleted!')
    return redirect(reverse('gallery'))
