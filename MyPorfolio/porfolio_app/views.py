from django.shortcuts import render,redirect

def home(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Resume(request):
    return render(request,'resume.html')

def Services(request):
    return render(request,'services.html')

def Porfolio(request):
    return render(request,'portfolio.html')

def Contact(request):
    return render(request,'contact.html')
