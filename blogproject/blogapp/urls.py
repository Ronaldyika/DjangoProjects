from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.index, name='index'),
    path('home/', user_views.home, name='home'),


    #_______________user_registration/login start______________________#
    path('register/', user_views.RegisterUser, name='register'),
    path('loginuser/', auth_views.LoginView.as_view(template_name='login/login.html'), name='loginuser'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    #_______________user_registration/login end______________________#



    #_______________blog_urls start______________________#
    path('blog_list/', user_views.blog_list, name='blog_list'),
    path('create/', user_views.blog_create, name='blog_create'),
    path('<int:pk>/', user_views.blog_detail, name='blog_detail'),
    path('<int:pk>/share/', user_views.blog_share, name='blog_share'),
    #_________________blog_urls end________________#
]