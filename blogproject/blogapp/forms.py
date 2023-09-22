from django.contrib.auth.forms import UserCreationForm;
from .models import Comment,BlogPost
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('blog','author','content')

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','content','author','is_published')