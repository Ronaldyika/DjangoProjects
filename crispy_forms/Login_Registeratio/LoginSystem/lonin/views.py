from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-signin')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

    
    