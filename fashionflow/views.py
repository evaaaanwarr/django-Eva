# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Page, Blog

def home(request):
    categories = Category.objects.all()
    pages = Page.objects.filter(is_published=True)
    posts = Blog.objects.filter(status=1)
    return render(request, 'home.html', {'categories': categories, 'pages': pages, 'posts': posts})

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def post_list(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'post_list.html', {'posts': posts})

def page_list(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'page_list.html', {'pages': pages})

def blog(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=1)
    return render(request, 'blog.html', {'post': post})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'page_detail.html', {'page': page})