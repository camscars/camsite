from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'personal/home_page.html')
def contact(request):
	return render(request, 'personal/basic.html', {'contact':['If you would like to contact me, please email me at:', 'cameronwoody702@gmail.com'], 'phone':['I can also be reached by phone at:', '702-496-xxxx']})
def projects(request):
	return render(request, 'personal/projects.html')