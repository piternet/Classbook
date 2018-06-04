from django import template
from main.models import Profile, Student
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_profile(user):
	return Profile.objects.get(user=user)

@register.simple_tag
def get_username(user, view_name, username):
	if view_name:
		return username
	else:
		return user.username

@register.simple_tag
def get_profile_description(user, view_name, username):
	if view_name:
		description = Profile.objects.get(user=User.objects.get(username=username)).description
	else:
		description = Profile.objects.get(user=user).description
	if description:
		return description
	else:
		return ""

@register.simple_tag
def get_profile_avatar(user, view_name, username):
	if view_name:
		avatar = Profile.objects.get(user=User.objects.get(username=username)).avatar
	else:
		avatar = Profile.objects.get(user=user).avatar
	if avatar:
		return avatar.url[4:]
	else:
		return '/static/main/avatars/default.png'

@register.simple_tag
def is_student(user):
	return Student.objects.get(profile=Profile.objects.get(user=user)).exists()

@register.simple_tag
def get_student_class(user):
	return Student.objects.get(profile=Profile.objects.get(user=user)).studentClass

@register.simple_tag
def get_user_post_type(user):
	if user.is_superuser:
		return "publiczny"
	elif get_student_class(user) == None:
		return " - najpierw wybierz klasę!"
	else:
		return "do klasy " + str(get_student_class(user))

@register.simple_tag
def get_post_class(post):
	if post.school == None:
		return "publiczny"
	elif post.postClass == None:
		return "ze szkoły " + str(post.school)
	else:
		return "z klasy " + str(post.postClass)

@register.simple_tag
def get_conversation_username(conversation, user):
	if conversation.user1 == user:
		return conversation.user2.username
	else:
		return conversation.user1.username