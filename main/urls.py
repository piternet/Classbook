from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
	url(r'^$', views.welcome_screen, name='welcome_screen'),
	url(r'^classbook/$', views.index, name='index'),
	url(r'^class_posts/$', views.class_posts, name='class_posts'),
	url(r'^tag/(?P<name>\w+)/$', views.tag_view, name="tag_view"),
	url(r'^user/(?P<name>\w+)/$', views.user_view, name="user_view"),
	url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
	url(r'^edit_class/$', views.edit_class, name="edit_class"),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^change_password/$', views.change_password, name='change_password'),
]
