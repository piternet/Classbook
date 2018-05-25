from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Profile, Student, School, Class, Teacher
from .forms import PostForm, ProfileForm, SignupForm, ClassInfoForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models.signals import post_save
from datetime import datetime

def welcome_screen(request):
	if request.user.is_authenticated:
		return redirect('index')
	return render(request, 'main/welcome/index.html')

@login_required(login_url='/')
def index(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			if form.cleaned_data['photo']:
				post.photo = form.cleaned_data['photo']
			post.publish_date = datetime.now()
			profile = Profile.objects.get(user=request.user)
			if profile.is_student():
				student = Student.objects.get(profile=profile)
				post.postClass = student.studentClass
				post.school = student.school
			if profile.is_teacher():
				teacher = Teacher.objects.get(profile=profile)
				post.school = teacher.school
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

@login_required(login_url='/')
def class_posts(request):
	profile = Profile.objects.get(user=request.user)
	if profile.is_student():
		student = Student.objects.get(profile=profile)
		posts = Post.objects.filter(postClass=student.studentClass)
	if profile.is_teacher():
		posts = Post.objects.all() # TODO - nauczyciel moglby miec ManyToManyField klas
	context = {
		'posts': posts,
	}
	return render(request, 'main/class_posts.html', context)

@login_required(login_url='/')
def tag_view(request, name):
	posts = Post.objects.filter(tags__name=name)
	context = {
		"name": name,
		"posts": posts
	}
	return render(request, 'search/tag_view.html', context)

@login_required(login_url='/')
def user_view(request, name):
	user = User.objects.get(username=name)
	posts = Post.objects.filter(user=user)
	context = {
		"username": name,
		"posts": posts
	}
	return render(request, 'main/user_view.html', context)

@login_required(login_url='/')
def edit_profile(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			if form.cleaned_data['avatar']:
				profile.avatar = form.cleaned_data['avatar']
			if form.cleaned_data['description']:
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

@login_required(login_url='/')
def edit_class(request):
	profile = Profile.objects.get(user=request.user)
	student = Student.objects.get(profile=profile)
	if request.method == 'POST':
		form = ClassInfoForm(request.POST)
		# todo: sprwadzic o co tu chodzi
		#if form.is_valid():
		student.studentClass = Class.objects.get(pk=form.data['studentClass'])
		student.save()
		return redirect('edit_class')

	form = ClassInfoForm(initial={
		'school': student.school,
		'studentClass': student.studentClass
	})
	form.fields['studentClass'].queryset = Class.objects.filter(school=student.school)
	context = {
		'form': form
	}
	return render(request, 'main/edit_class.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('change_password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'accounts/change_password.html', {
		'form': form
	})

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
			return redirect('index')
		else:
			return redirect('signup')
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