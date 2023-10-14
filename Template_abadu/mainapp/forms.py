from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gallery,UpcomingEvent,BlogPost

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class GalleryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter block title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'image']
class UpcomingEventForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvent
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }