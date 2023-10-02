from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

#router.register('fbviews',views.BookListApiview)

urlpatterns = [
    #path('api/',include(router.urls))
    path('',views.BookList.as_view(),name="Books"),
    path('bookdetails/<int:pk>/',views.BookDetail.as_view(),name='bookdetails'),
    path('creditlist/',views.CreditBookList.as_view(),name='creditlist'),
    path('creditdetails/<int:pk>/',views.CreditBookdetail.as_view(),name='creditdetails'),
]