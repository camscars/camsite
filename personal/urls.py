from django.shortcuts import render
from django.conf.urls import url
from . import views
# . imports from the current package. It is relative

# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name ='contact'),
    url(r'^projects/$', views.projects, name='projects'),

]