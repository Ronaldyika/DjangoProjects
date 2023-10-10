from django.shortcuts import render,redirect
from .forms import GalleryForm,UpcomingEventForm,UserRegistrationForm
from django.contrib.auth.models import User
from django.views import View
from .models import Gallery,UpcomingEvent

def homepage(request):
    return render(request,'index.html')

def aboutpage(request):
    return render(request,'partials/about.html')

def actionplan(request):
    return render(request,'partials/actionplan.html')

#-------------------------registration section--------------------------------
def AdminRegistrationView(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('AdminLogin')
    else:
        return render(request,'authentication/register.html',{'form':form}) 
    

#---------------------------------gallery and upcoming task-----------------------
def AdminGallery(request):
    form = GalleryForm()
    posts = Gallery.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
    if form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        image = form.cleaned_data['image']
        gallery = Gallery(title=title, description=description, image=image)
        gallery.save()
        return redirect('admingallery')
    else:
        return render(request, 'admin_pannel/gallery.html', {'form': form,'posts':posts})
    
