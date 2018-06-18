from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Conversation
from .serializers import ConversationSerializer

class ConversationList(APIView):

	def get(self, request, id):
		conversation = Conversation.objects.get(id=int(id))
		serializer = ConversationSerializer(conversation)
		return Response(serializer.data)
