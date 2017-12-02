from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=10000)
	publish_date = models.DateField()
	user = models.ForeignKey(User)

	def __str__(self):
		return "Tytul: " + self.title + ", Tresc: " + self.content

	class Meta:
		ordering = ['-publish_date', 'title']