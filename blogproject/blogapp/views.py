from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def index(request):
    return render(request,'main/index.html')

@login_required()
def home(request):
    return render(request,'main/home.html')

def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginuser')
    else:
        form = RegisterUserForm()
    
    return render(request, 'login/register.html', {'form': form})
