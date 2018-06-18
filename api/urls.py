from django.conf.urls import url, include
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
	url(r'^conversation/(?P<id>\d+)/$', views.ConversationList.as_view(), name='conversation_list'),
]
