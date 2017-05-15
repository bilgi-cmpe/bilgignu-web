from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/home.html', {"posts": posts})

def detail(request, pattern):
    post = Post.objects.get(pattern=pattern)
    return render(request, 'blog/detail.html', {"post": post})
