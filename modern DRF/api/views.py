from django.shortcuts import render,redirect
from .serializer import UserSerializer,BookSerializer,CreditBookSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Book,CreditBook
from rest_framework.generics import GenericAPIView,get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
#===========generic CBV ==================

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreditBookList(generics.ListCreateAPIView):
    queryset = CreditBook.objects.all()
    serializer_class = CreditBookSerializer

class CreditBookdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditBook.objects.all()
    serializer_class = CreditBookSerializer