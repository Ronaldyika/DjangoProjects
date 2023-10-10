from django.contrib.staticfiles.views import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
   re_path(r'^static/(?P<mainproject>.*)$',serve),
]

urlpatterns += staticfiles_urlpatterns()