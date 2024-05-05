# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category, name='category'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/<slug:slug>/', views.contact, name='contact'),
    path('hijabstyle/', views.hijabstyle, name='hijabstyle'),
    path('fashiontrends/', views.fashiontrends, name='fashiontrends'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),
]
