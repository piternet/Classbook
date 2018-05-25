from django import forms
from .models import Post, Profile, School, Class
from django.contrib.auth import (
	authenticate, get_user_model, password_validation,
)

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

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['description', 'avatar']
		widgets = {
			'description': forms.Textarea(attrs={'cols': 50, 'rows': 1})
		}
		labels = {
			'description': 'Opis'
		}

class ClassInfoForm(forms.Form):
	school = forms.ModelChoiceField(queryset=School.objects.all(), label="Szkoła", disabled=True)
	studentClass = forms.ModelChoiceField(queryset=Class.objects.all(), label="Klasa")

class SignupForm(forms.Form):
	username = forms.CharField(max_length=256, label="Nazwa użytkownika")
	email = forms.CharField(max_length=256, label="Adres email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Hasło")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Powtórz hasło")
	status = forms.ChoiceField(choices=(('student', 'Uczeń'), ('teacher', 'Nauczyciel'), ('boss', 'Dyrektor')))
	school = forms.ModelChoiceField(queryset=School.objects.all(), label="Szkoła")

	error_messages = {
		'password_mismatch': "Hasła nie zgadzają się.",
	}

	def is_valid(self):
		valid = super(SignupForm, self).is_valid()
		if not valid:
			return False

		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
			return False

		return True