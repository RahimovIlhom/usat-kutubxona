from django.conf import settings
from rest_framework import serializers

from library.models import Book, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    book_link = serializers.SerializerMethodField('get_book_file_url')

    class Meta:
        model = Book
        fields = ['id', 'category', 'title', 'sub_title', 'author', 'book_link', 'isbn', 'create_time', 'update_time']

    def get_category(self, obj):
        return CategorySerializer(obj.category).data

    def get_book_file_url(self, obj):
        request = self.context.get("request")
        if obj.book_file:
            return request.build_absolute_uri(obj.book_file.url)
        return obj.book_link or "No link available"


class BooksRelatedToCategoriesSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField('get_books')

    class Meta:
        model = Category
        fields = ['id', 'name', 'books']

    def get_books(self, obj):
        books = Book.objects.filter(category__id=obj.id)
        return BookSerializer(books, many=True, context=self.context).data
