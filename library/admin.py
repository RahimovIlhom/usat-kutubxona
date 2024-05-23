from django.contrib import admin

from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'book_link', 'book_file']
    list_filter = ['category']
    search_fields = ['title', 'category__name', 'author', 'isbn']


admin.site.register(Category)
admin.site.register(Book, BookAdmin)
