from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db import models
from datetime import datetime

# TODO:
# 1. dodawanie nowch komentarzy do postow:
	# - albo nowy widok albo w indexie przy postach
	# - formularz w forms.py
	# pamietaj zeby w jakis sposb wiedziec do ktorego tagu dodajesz komentarz
	# post.comments.add(comment)
# 2. dodawnie nowych tagow
	# - w menu link dodaj nowy tag
	# - mozliwosc dodanai prez uzytkownikow nowych tagow

def index(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.publish_date = datetime.now()
			post.save()
			tags = form.cleaned_data['tags']
			for tag in tags:
				post.tags.add(tag)
			post.save()
			return HttpResponseRedirect('/')
	form = PostForm()
	posts = Post.objects.all()
	context = {
		'posts': posts,
		'form': form
	}
	return render(request, 'main/index.html', context)

def tag_view(request, name):
	posts = Post.objects.filter(tags__name=name)
	context = {
		"name": name,
		"posts": posts
	}
	return render(request, 'search/tag_view.html', context)


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

