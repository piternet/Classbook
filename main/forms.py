from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'tags']
		widgets = {
			'title': forms.Textarea(attrs={'cols': 50, 'rows': 1, 'placeholder': 'Jak zatytułujesz swój post?'}),
			'content': forms.Textarea(attrs={'cols': 50, 'rows': 6, 'placeholder': 'Cześć, co u ciebie słychać? Podziel się tym z nami.'})
		}
		labels = {
			'title': 'Tytuł',
			'content': 'Zawartość',
			'tags': 'Tagi'
		}