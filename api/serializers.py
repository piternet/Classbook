from rest_framework import serializers
from main.models import Conversation, Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('username')

class MessageSerializer(serializers.ModelSerializer):
	sender = serializers.SlugRelatedField(
		read_only = True,
		slug_field = 'username'
	)
	class Meta:	
		model = Message
		fields = ('date', 'content', 'sender')


class ConversationSerializer(serializers.ModelSerializer):
	user1 = serializers.SlugRelatedField(
		read_only = True,
		slug_field = 'username'
	)
	user2 = serializers.SlugRelatedField(
		read_only = True,
		slug_field = 'username'
	)
	messages = MessageSerializer(read_only=True, many=True)
	class Meta:
		model = Conversation
		fields = ('user1', 'user2', 'messages')

