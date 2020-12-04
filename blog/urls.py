#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" blog/urls.py"""

from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #pk means primary key
    path('', BlogListView.as_view(), name='home'), #home page view
    
]