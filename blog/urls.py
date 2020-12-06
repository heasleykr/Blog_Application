#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" blog/urls.py"""

from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView, 
    BlogUpdateView,
    BlogDeleteView,)

urlpatterns = [
    path('post/<int:pk>/delete/', 
        BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', 
        BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #pk means primary key
    path('', BlogListView.as_view(), name='home'), #home page view
    
]