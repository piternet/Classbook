from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class School(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name

class Class(models.Model):
	grade = models.IntegerField()
	name = models.CharField(max_length=1)
	school = models.ForeignKey(School, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.grade) + self.name # + " w szkole " + self.school.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='main/static/main/avatars/', blank=True, null=True)
	description = models.CharField(max_length=1024, blank=True, null=True)

	def __str__(self):
		return self.user.username

class Student(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	school =  models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)
	studentClass = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.profile.user.username + " w szkole " + self.school.name

class Tag(models.Model):
	name = models.CharField(max_length=80)

	def __str__(self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(default=datetime.now) # DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=300)

	def __str__(self):
		return self.content[:50]
	
class Post(models.Model):
	title = models.CharField(max_length=150)
	content = models.CharField(max_length=10000)
	publish_date = models.DateField(default=datetime.now) # DateTimeField(auto_now_add=True)
#	edit_date = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
	comments = models.ManyToManyField(Comment)
	photo = models.ImageField(upload_to='main/static/main/imgs/', blank=True, null=True)

	school = models.ForeignKey(School, null=True, blank=True)
	postClass = models.ForeignKey(Class, null=True, blank=True)

	def __str__(self):
		return "Tytul: " + self.title + ", Tresc: " + self.content

	class Meta:
		ordering = ['-publish_date', 'title']

