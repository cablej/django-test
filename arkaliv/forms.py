from django import forms

from .models import File

class PostForm(forms.ModelForm):

	class Meta:
		model = File
		fields = ('title', 'text',)