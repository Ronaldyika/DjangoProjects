from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gallery,UpcomingEvent,BlogPost

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

class UpcomingEventForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvent
        fields = '__all__'
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'