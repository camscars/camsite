from django.shortcuts import render
from .models import Entry

# Create your views here.

def blog(request):
	article = Entry.objects.all()
	return render(request, "blog/home.html", {"article" : article})

def blog_page(request):
	article = Entry.objects.all()
	return render(request, "blog/blog_pages.html", {"article": article})

def home_page(request):
	return render(request, "personal/home_page.html")