from django import forms
from .models import Post, Student

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'photo', 'tags']
		widgets = {
			'title': forms.Textarea(attrs={'cols': 50, 'rows': 1, 'placeholder': 'Jak zatytułujesz swój post?'}),
			'content': forms.Textarea(attrs={'cols': 50, 'rows': 6, 'placeholder': 'Cześć, co u ciebie słychać? Podziel się tym z nami.'})
		}
		labels = {
			'title': 'Tytuł',
			'content': 'Zawartość',
			'photo': 'Wybierz zdjęcie (opcjonalnie)',
			'tags': 'Tagi'
		}

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['description', 'avatar']
		widgets = {
			'description': forms.Textarea(attrs={'cols': 50, 'rows': 1})
		}
		labels = {
			'description': 'Opis'
		}