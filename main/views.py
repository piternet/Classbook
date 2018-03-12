from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db import models
from datetime import datetime

def index(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			if form.cleaned_data['photo']:
				post.photo = form.cleaned_data['photo']
			post.publish_date = datetime.now()
			post.save()
			tags = form.cleaned_data['tags']
			for tag in tags:
				post.tags.add(tag)
			post.save()
			return redirect('index')
		else:
			messages.add_message(request, messages.ERROR, 'Błąd w formularzu. Proszę spróbowac jeszcze raz.')
			return redirect('index')
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

