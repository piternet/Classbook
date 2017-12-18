from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tag(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey(User)
	date = models.DateField(default=datetime.now) # DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=300)

	def __str__(self):
		return self.content[:50]
	
class Post(models.Model):
	title = models.CharField(max_length=150)
	content = models.CharField(max_length=10000)
	publish_date = models.DateField(default=datetime.now) # DateTimeField(auto_now_add=True)
#	edit_date = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)
	comments = models.ManyToManyField(Comment)

	def __str__(self):
		return "Tytul: " + self.title + ", Tresc: " + self.content

	class Meta:
		ordering = ['-publish_date', 'title']
