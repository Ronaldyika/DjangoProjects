from django.contrib.staticfiles.views import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,re_path
from . import views
from .views import AdminRegistrationView,UserViewdetials,UserViewUpcoming,AdminUpdateDeleteView
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name='home'),
   re_path(r'^static/(?P<mainproject>.*)$',serve),
   path('about/',views.aboutpage,name='about'),
   path('action_plan/',views.actionplan,name='actionplan'),

   #---------------------------registration-----------------------

   path('admin_registration/',views.AdminRegistrationView,name='AdminRegistration'),
   path('loginabadu_admin/',auth_views.LoginView.as_view(template_name = 'authentication/login.html'),name='AdminLogin'),
   path('logoutabadu_admin',auth_views.LogoutView.as_view(template_name = 'authentication/logout.html'),name='AdminLogOut'),


   #--------------------------admin uploads-----------------------
   path('adminpannel/gallery',login_required(views.AdminGallery),name='admingallery'),
   path('adminpannel/upcoming',login_required(views.UpcomingTask),name='UpcomingTask'),
   path('gallery/update/<int:pk>/', login_required(AdminUpdateDeleteView.as_view()), name='update_gallery'),
   path('gallery/delete/<int:pk>/', login_required(AdminUpdateDeleteView.as_view()), name='delete_gallery'),


   #------------------------------user urls----------------------------------------

   path('gallery/',views.UserViewdetials.as_view(),name='usergallery'),
   path('upcomging/',views.UserViewUpcoming.as_view(),name='userupcoming')

]

urlpatterns += staticfiles_urlpatterns()



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 