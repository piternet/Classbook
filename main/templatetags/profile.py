from django import template
from main.models import Profile

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