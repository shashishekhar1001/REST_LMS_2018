from django import forms
from .models import *
import datetime

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "title",
            "content",
            "publish"
        ]

class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=120)
    image = forms.ImageField(required=False)
    content = forms.CharField(required=True, widget=forms.Textarea)
    draft = forms.BooleanField()