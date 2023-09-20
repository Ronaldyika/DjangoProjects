from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.http import HttpResponse

def index(request):
    return render(request,'main/index.html')

def home(request):
    return render(request,'main/home.html')


def RegisterUser(request):
    form = RegisterUserForm()

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            print("The form is valid and saved successfully.")

    else:
        context = {
            'form': form
        }
        return render(request, 'login/register.html', context)