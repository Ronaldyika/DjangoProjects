from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.index, name='index'),
    path('home/', user_views.home, name='home'),
    path('register/', user_views.RegisterUser, name='register'),
    path('loginuser/', auth_views.LoginView.as_view(template_name='login/login.html'), name='loginuser'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
]