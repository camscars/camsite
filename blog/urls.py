from django.shortcuts import render
from django.conf.urls import patterns, url
from . import views
from . import models

# Create your views here.

urlpatterns = [
	url(r'^$', views.blog, name='blog'),
	url(r'.*', views.blog_page, name='blog_page'),
	url(r'^$', views.home_page, name='home_page'),
]