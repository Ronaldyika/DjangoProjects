from django.urls import path,re_path
from . import views as user_view
from django.contrib.staticfiles.views import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',user_view.home,name='index'),
    path('About/',user_view.About,name='about'),
    path('Resume/',user_view.Resume,name='resume'),
    path('Services/',user_view.Services,name='services'),
    path('Portfolio/',user_view.Porfolio,name='portfolio'),
    path('contact/',user_view.Contact,name='contact'),
    re_path(r'^static/(?P<MyPorfolio>.*)$',serve)

]
urlpatterns += staticfiles_urlpatterns()