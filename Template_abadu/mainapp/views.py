from django.shortcuts import render,redirect

def homepage(request):
    return render(request,'index.html')

def aboutpage(request):
    return render(request,'partials/about.html')

def actionplan(request):
    return render(request,'partials/actionplan.html')