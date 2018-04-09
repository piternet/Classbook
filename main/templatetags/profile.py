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

@register.simple_tag
def get_user_post_type(user):
	if user.is_superuser:
		return "publiczny"
	elif get_student_class(user) == None:
		return " - nie jesteś w żadnej klasie, najpierw wybierz klasę!"
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