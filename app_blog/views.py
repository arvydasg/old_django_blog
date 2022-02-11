from django.shortcuts import render
from .models import Post


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'app_blog/frontpage.html', {'posts': posts})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'app_blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'app_blog/post_detail.html', {'post': post})
