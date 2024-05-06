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

def blog(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'blog.html', {'posts': posts})

def about(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'about.html', {'pages': pages})

def contact(request):
    return render(request, 'contact.html', {'contact': contact})

def fashiontrends(request):
    return render(request, 'fashiontrends.html')

def hijabstyle(request):
    return render(request, 'hijabstyle.html')

def makeuptrends(request):
    return render(request, 'makeuptrends.html')

def category_tops(request):
    return render(request, 'category_tops.html')

def category_bottoms(request):
    return render(request, 'category_bottoms.html')

def category_outerwear(request):
    return render(request, 'category_outerwear.html')

def category_abayas(request):
    return render(request, 'category_abayas.html')

def category_hijabs(request):
    return render(request, 'category_hijabs.html')

def category_accessories(request):
    return render(request, 'category_accessories.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'page_detail.html', {'page': page})