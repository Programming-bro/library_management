from django.db import models
from books.models import Book
from users.models import Member

# Create your models here.

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed')
    member = models.ForeignKey(Member, on_delete=models.CASCADE ,related_name='borrowed_by')
    borrow_date = models.DateTimeField(auto_created=True)
    return_date = models.DateTimeField()