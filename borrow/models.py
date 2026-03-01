from django.db import models
from books.models import Book
from django.conf import settings
# Create your models here.

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE ,related_name='borrowed')
    borrow_date = models.DateTimeField(auto_created=True)
    return_date = models.DateTimeField()