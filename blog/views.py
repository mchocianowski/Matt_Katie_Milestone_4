from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Category_blog
from .forms import BlogForm
# Create your views here.


def all_posts(request):
    posts = Post.objects.all()
    category_blog = None

    if request.GET:
        if 'category_blog' in request.GET:
            category_blog = request.GET['category_blog'].split(',')
            posts = posts.filter(category_blog__name__in=category_blog)
            category_blog = Category_blog.objects.filter(name__in=category_blog)

    context = {
        'posts': posts,
        'category_blog': None
    }
    return render(request, 'blog/blog.html', context)


def post_detail(request, post_id):
    """ A view to show individual blog posts """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    """ Add a post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = BlogForm()
       
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated image and title!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update image. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))


