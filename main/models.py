from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=10000)
	publish_date = models.DateField()
	user = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return "Tytul: " + self.title + ", Tresc: " + self.content

	class Meta:
		ordering = ['-publish_date', 'title']