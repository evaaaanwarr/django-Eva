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
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
]
