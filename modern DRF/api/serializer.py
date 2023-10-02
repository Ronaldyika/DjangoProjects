from .models import Book,CreditBook
from django.contrib.auth.models import User
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CreditBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditBook
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'