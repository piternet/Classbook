from django.contrib import admin
from .models import Post, Tag, Comment, School, Class, Profile, Student, Conversation, Message

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Conversation)
admin.site.register(Message)