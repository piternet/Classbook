from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Profile, Student, School, Class
from .forms import PostForm, ProfileForm, SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import models
from django.db.models.signals import post_save
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

def edit_profile(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.avatar = form.cleaned_data['avatar']
			profile.description = form.cleaned_data['description']
			profile.save()
			return redirect('edit_profile')

	form = ProfileForm(initial={
		'description': profile.description,
		'avatar': profile.avatar
	})
	context = {
		'form': form
	}
	return render(request, 'main/edit_profile.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			status = form.cleaned_data['status']
			school = form.cleaned_data['school']

			user = User(username=username, password=password, email=email)
			user.save()
			profile = Profile.objects.get(user=user)

			if status == 'student':
				student = Student(profile=profile, school=school)
				student.save()

			login(request, user)
			return HttpResponseRedirect('/')
	form = SignupForm()
	context = {
		"form": form
	}
	return render(request, 'registration/signup.html', context)

def create_profile(sender, **kwargs):
	user = kwargs['instance']
	if kwargs['created']:
		profile = Profile(user=user)
		profile.save()


post_save.connect(create_profile, sender=User)