from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db import models

# Create your views here.
def index(request):
	posts = Post.objects.all()
	context = {
		'posts': posts
	}
	return render(request, 'main/index.html', context)

def tag_view(request, name):
	# PRACA DOMOWA:
	# napisac ten widok tak, zeby wyswietlal wszystkie posty, ktore sa otagowane tym tagiem
	# trzeba skorzystac z Post.objects.filter(tags__name=name)
	posts = Post.objects.filter(tags__name=name)
	context = {
		"name": name,
		"posts": posts
	}
	return render(request, 'search/tag_view.html', context)
# PRACA DOMOWA 2:
# analogicznie do tag_view napisac user_view
# urls, views, templates

def user_view(request, name):
	user = User.objects.get(username=name)
	posts = Post.objects.filter(user=user)
	context = {
		"username": name,
		"posts": posts
	}
	return render(request, 'main/user_view.html', context)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect('/')
	form = UserCreationForm()
	context = {
		"form": form
	}
	return render(request, 'registration/signup.html', context)

