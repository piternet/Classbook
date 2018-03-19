from django import template
from main.models import Student

register = template.Library()

@register.simple_tag
def get_student(user):
	return Student.objects.get(user=user)

@register.simple_tag
def get_student_description(user):
	return Student.objects.get(user=user).description

@register.simple_tag
def get_student_avatar(user):
	avatar = Student.objects.get(user=user).avatar
	if avatar:
		return avatar.url[4:]
	else:
		return '/static/main/avatars/default.png'