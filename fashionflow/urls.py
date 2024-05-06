# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hijabstyle/', views.hijabstyle, name='hijabstyle'),
    path('fashiontrends/', views.fashiontrends, name='fashiontrends'),
    path('makeuptrends/', views.makeuptrends, name='makeuptrends'),
    path('category_tops/', views.category_tops, name='category_tops'),
    path('category_bottoms/', views.category_bottoms, name='category_bottoms'),
    path('category_outerwear/', views.category_outerwear, name='category_outerwear'),
    path('category_abayas/', views.category_abayas, name='category_abayas'),
    path('category_hijabs/', views.category_hijabs, name='category_hijabs'),
    path('category_accessories/', views.category_accessories, name='category_accesories'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
]
