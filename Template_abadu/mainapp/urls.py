from django.contrib.staticfiles.views import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,re_path
from . import views
from .views import AdminRegistrationView
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.homepage,name='home'),
   re_path(r'^static/(?P<mainproject>.*)$',serve),
   path('about/',views.aboutpage,name='about'),
   path('action_plan/',views.actionplan,name='actionplan'),

   #---------------------------registration-----------------------

   path('admin_registration/',views.AdminRegistrationView,name='AdminRegistration'),
   path('loginabadu_admin/',auth_views.LoginView.as_view(template_name = 'authentication/login.html'),name='AdminLogin'),
   path('logOutabadu_admin/',auth_views.LoginView.as_view(template_name = 'index.html'),name='AdminLogOut'),


   #--------------------------admin uploads-----------------------
   path('adminpannel/gallery',login_required(views.AdminGallery),name='admingallery'),
]

urlpatterns += staticfiles_urlpatterns()