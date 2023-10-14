from django.shortcuts import get_object_or_404, render,redirect
from .forms import GalleryForm,UpcomingEventForm,UserRegistrationForm,BlogPostForm
from django.contrib.auth.models import User
from django.views import View
from .models import Gallery,UpcomingEvent,BlogPost

def homepage(request):
    posts = BlogPost.objects.all()

    counter = posts.count()

    return render(request,'index.html',{'counter':counter})

def aboutpage(request):
    posts = BlogPost.objects.all()

    counter = posts.count()
    return render(request,'partials/about.html',{'counter':counter})

def actionplan(request):
    posts = BlogPost.objects.all()

    counter = posts.count()
    return render(request,'partials/actionplan.html',{'counter':counter})

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

def UpdateGallery(request, pk):
    item = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admingallery')
    else:
        form = GalleryForm(instance=item)
    return render(request, 'admin_pannel/gallery.html', {'form': form, 'item': item})

#-----------------------delete function-------------------------------    
def deleteblog(request,pk):
    item = Gallery.objects.filter(pk=pk)
    item.delete()
    return redirect('admingallery')

#-----------------------------upcoming update function---------------------
def UpdateUpcomingEvents(request, pk):
    item = get_object_or_404(UpcomingEvent, pk=pk)
    if request.method == 'POST':
        form = UpcomingEventForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('UpcomingTask')
    else:
        form = GalleryForm(instance=item)
    return render(request, 'admin_pannel/upcoming.html', {'form': form, 'item': item})


#---------------------------------delete upcoming event------------------------
def deleteUpcoming(request,pk):
    item = UpcomingEvent.objects.filter(pk=pk)
    item.delete()
    return redirect('UpcomingTask')

#-------------------------------------update blogs---------------------------------
def UpdateBlogs(request, pk):
    item = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('blogpost')
    else:
        form = BlogPost()
    return render(request, 'admin_pannel/blog.html', {'form': form, 'item': item})


#---------------------------------delete blogs------------------------
def DeleteBlogs(request,pk):
    item = BlogPost.objects.filter(pk=pk)
    item.delete()
    return redirect('blogpost')

#-----------------------------------admin gallery--------------------------
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
    
def UpcomingTask(request):
    form = UpcomingEvent()
    posts = UpcomingEvent.objects.all()
    if request.method == 'POST':
        form = UpcomingEventForm(request.POST,request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            upcoming = UpcomingEvent(description=description,image = image)
            upcoming.save()
            return redirect('UpcomingTask')
    else:
        return render(request,'admin_pannel/upcoming.html',{'form':form,'posts':posts})

#--------------------------------customer section-------------------------------------
class UserViewdetials(View):
    def get(self,request):
        posts = BlogPost.objects.all()

        counter = posts.count()
        posts = Gallery.objects.all()
        return render(request,'partials/gallery.html',{'posts':posts,'counter':counter})
    
    
class UserViewUpcoming(View):
    def get(self,request):
        posts = UpcomingEvent.objects.all()
        post = BlogPost.objects.all()
        counter = post.count()

        return render(request,'partials/upcoming.html',{'posts':posts,'counter':counter})
    

def donation(request):
    posts = BlogPost.objects.all()

    counter = posts.count()
    return render(request,'partials/donate.html',{'counter':counter})

#-------------------------blogpost----------------------------------------------

class AdminBlogPostView(View):
    def get(self, request):
        posts = BlogPost.objects.all()
        form = BlogPostForm()
        return render(request, 'admin_pannel/blog.html', {'form': form, 'posts': posts})

    def post(self, request):
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost')

        posts = BlogPost.objects.all()
        form = BlogPostForm()
        return render(request, 'admin_pannel/blog.html', {'form': form, 'posts': posts})

def userblog(request):
    
    posts = BlogPost.objects.all()
    counter = posts.count()

    return render(request,'partials/userblog.html',{'posts':posts,'counter':counter})