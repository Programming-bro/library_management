from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='written_by')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    available_quantity = models.IntegerField()
