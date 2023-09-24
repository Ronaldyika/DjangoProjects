from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import registerForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("this form is created")
    else:
        form = registerForm()
        return render(request,"register.html",{'form':form})

def signup(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(request,"user created succesfully")
    else:
        form = registerForm()

        return render(request,'register.html',{"form":form})