from django.contrib import admin
from books.models import Book, Category, Author
from borrow.models import Borrow
from users.models import User

# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Borrow)
admin.site.register(User)