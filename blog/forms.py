from django import forms
from .models import Blog, Image

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','body',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)