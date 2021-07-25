from django.shortcuts import render, get_object_or_404
from .models import Post, Category_blog

# Create your views here.


def all_posts(request):
    posts = Post.objects.filter(status=1)
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
