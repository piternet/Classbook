from django import template
from main.models import Profile, Student

register = template.Library()

@register.simple_tag
def get_profile(user):
	return Profile.objects.get(user=user)

@register.simple_tag
def get_profile_description(user):
	return Profile.objects.get(user=user).description

@register.simple_tag
def get_profile_avatar(user):
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

