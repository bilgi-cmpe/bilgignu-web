from django.shortcuts import render
from .models import Post, Category
from django.http import HttpResponseRedirect

def home(request):
    posts = Post.objects.all().order_by("-date")
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {"posts": posts, "categories": categories})


def detail(request, pattern):
    post = Post.objects.get(pattern=pattern)
    categories = Category.objects.all()
    return render(request, 'blog/detail.html', {"post": post, "categories": categories})


def category(request, pattern):
    page = Category.objects.get(pattern=pattern)
    if page.redirect:
        return HttpResponseRedirect(page.url)
    categories = Category.objects.all()
    return render(request, 'blog/detail.html', {"categories": categories})
