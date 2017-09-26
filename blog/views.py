from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View

from .models import Post, Category

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all().order_by("-date")
        categories = Category.objects.all()
        return render(request, 'blog/home.html', {"posts": posts, "categories": categories})


class DetailView(View):
    def get(self, request):
        post = Post.objects.get(pattern=pattern)
        categories = Category.objects.all()
        return render(request, 'blog/detail.html', {"post": post, "categories": categories})


class CategoryView(View):
    def get(self, request):
        page = Category.objects.get(pattern=pattern)
        if page.redirect:
            return HttpResponseRedirect(page.url)
        categories = Category.objects.all()
        return render(request, 'blog/detail.html', {"categories": categories})
