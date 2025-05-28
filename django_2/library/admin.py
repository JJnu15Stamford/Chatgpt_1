# from import admin 
# from . import Author, Book

# admin.site.register(Author)
# admin.site.register(Book) 

from django.contrib import admin
from .models import Book  # or any model you have

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title',)

admin.site.register(Book, BookAdmin)
