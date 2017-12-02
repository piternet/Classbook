from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	app_name = 'kazekbook'
	context = {
		'app_name': app_name
	}
	return render(request, 'main/index.html', context)