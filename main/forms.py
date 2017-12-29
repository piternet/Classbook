from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'tags']
		widgets = {
			'content': forms.Textarea(attrs={'cols': 30, 'rows': 10})
		}
		labels = {
			'title': 'Tytuł',
			'content': 'Zawartość',
			'tags': 'Tagi'
		}