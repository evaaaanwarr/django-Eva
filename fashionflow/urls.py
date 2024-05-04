# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category, name='category_list'),
    path('posts/', views.post_list, name='post_list'),
    path('pages/', views.page_list, name='page_list'),
    path('blog/<slug:slug>/', views.blog, name='blog_detail'),  # Changed from 'post' to 'blog'
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
]
