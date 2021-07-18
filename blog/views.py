from django.shortcuts import render
from .models import Post

# Create your views here.


def all_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)