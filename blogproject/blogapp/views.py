from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterUserForm,BlogPostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import BlogPost,BlogShare,Comment,UserProfile
        
#--------------------------#index start------------------------#

def index(request):
    return render(request,'main/index.html')

#----------------------------index end--------------------------#
#=====================home start===============================#
@login_required()
def home(request):
    return render(request,'main/home.html')

#=====================home end=================================#
#==========================Registration============================#
def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginuser')
    else:
        form = RegisterUserForm()
    
    return render(request, 'login/register.html', {'form': form})
#==========================Registration end============================#


#_________________________________blogs start__________________________#
@login_required()
def blog_list(request):
    blog = BlogPost.objects.filter(is_published = True).order_by('created_at')  
    return render(request,'blog/blog_list.html',{'blog':blog})

@login_required()
def blog_detail(request,pk):
    blog = get_object_or_404(BlogPost,pk=pk,is_published = True)
    comment = Comment.objects.filter(blog = blog).order_by('created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_detail',pk=pk)
    else:
        form = CommentForm()
        return render(request,"blog/blog_detail.html",{'form':form,'comment':comment})


@login_required()
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
        return render(request,'blog/blog_create.html',{'form':form})
    
@login_required()
def blog_share(request,pk):
    blog = get_object_or_404(BlogPost,pk=pk)
    if request.method == 'POST':
        return  redirect('blog_detail',pk=pk)
    return render(request,'blog/blog_share.html',{'blog':blog})

#_________________________________blogs end__________________________#


#_______________________________comment section_____________________#
def comment(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    comments = blog.comments.all()
    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blog/comment.html', context)
#_______________________________end comment section_____________________#


#============================start of userprofile=======================#

def userprofile(request, user_id):
    userprofile = get_object_or_404(UserProfile, user_id=user_id)
    context = {
        'userprofile': userprofile,
    }
    return render(request, 'userprofile.html', context)
#============================start of userprofile=======================#
