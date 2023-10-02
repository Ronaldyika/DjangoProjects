from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    Name = models.CharField(max_length=255)
    Author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    Title = models.CharField(max_length=255)
    date_published = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{Name} publishedby {Author}"
    
class CreditBook(models.Model):
    BorrowedBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    libarian = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date_borrowed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{BorrowedBook.Name} was borrowed"    