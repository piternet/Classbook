from django import forms
from .models import Post, Profile, School, Class

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

class SignupForm(forms.Form):
	username = forms.CharField(max_length=256, label="Nazwa użytkownika")
	email = forms.CharField(max_length=256, label="Adres email")
	password1 = forms.CharField(widget=forms.PasswordInput, label="Hasło")
	password2 = forms.CharField(widget=forms.PasswordInput, label="Powtórz hasło")
	status = forms.ChoiceField(choices=(('student', 'Uczeń'), ('teacher', 'Nauczyciel'), ('boss', 'Dyrektor')))
	school = forms.ModelChoiceField(queryset=School.objects.all(), label="Szkoła")

	def is_valid(self):
		valid = super(SignupForm, self).is_valid()
		if not valid:
			return False

		# if self.password1 != self.password2:
		# 	self._errors['invalid_password'] = 'Hasła się nie zgadzają'
		# 	return False

		return True